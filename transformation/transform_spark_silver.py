# Import do Spark Sessions
from pyspark.sql import SparkSession
# Import de funcoes importantes do sparkSQL
from pyspark.sql.functions import col
# Import de funcoes uteis
from utils.utils import *
# Adicionado para lidar com o config.properties
import configparser
# Import do delta para configuracao do delta lake
from delta import configure_spark_with_delta_pip


config = configparser.ConfigParser()
config.read("config.properties")


class SparkDataTransformer:
    def __init__(self):

        # Inicializa o SparkSession
       builder = SparkSession.builder \
            .appName("SparkDataTransformerSilver") \
            .config("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension") \
            .config("spark.sql.catalog.spark_catalog", "org.apache.spark.sql.delta.catalog.DeltaCatalog") \
            .getOrCreate()

        self.spark = configure_spark_with_delta_pip(builder).getOrCreate()

        # Carregamento e tratamento de nulos e duplicados
        # Dataset provider do postgres
        provider_spark_df  = spark.read.parquet(config["POSTGRES_PROVIDER_BRONZE"])
        provider_spark_df = provider_spark_df \
            .dropna(subset=["provider_id", "provider_name", "care_site_id"]) \   # Remove linhas com nulos nessas colunas
            .fillna({"coluna_importante": "valor_padrao_estabelecido"}) \        # Preenche valores nulos na coluna 'xpto'
            .dropDuplicates(["provider_id"])

        # Dataset cote_site
        care_site_spark_df = spark.read.parquet(config["POSTGRES_CARE_SITE_BRONZE"])        
        
        care_site_spark_df = care_site_spark_df \
            .dropna(subset=["care_site_id", "care_site_name"]) \                  
            .fillna({"coluna_importante": "valor_padrao_estabelecido"}) \         
            .dropDuplicates(["care_site_id"]) 
        
        # Dataset provider do S3
        s3_provider_spark_df = spark.read.parquet(config["S3_PROVIDER_BRONZE"])
        s3_provider_spark_df = s3_provider_spark_df \
            .dropna(subset=["NPI", "Specialty"]) \                            
            .fillna({"coluna_importante": "valor_padrao_estabelecido"}) \                               
            .dropDuplicates(["NPI"]) 

        # Join entre os DataFrames, primeiro provider com care_site
        joined_df = provider_spark_df.join(
            care_site_spark_df,
            provider_spark_df["care_site_id"] == care_site_spark_df["care_site_id"],
            "inner"
        ).select(
            provider_spark_df["provider_id"],
            provider_spark_df["provider_name"],
            provider_spark_df["npi"],
            care_site_spark_df["care_site_name"]
        )

        # Integrar com os dados do S3
        joined_df = joined_df.join(
            s3_provider_spark_df,
            joined_df["npi"] == s3_provider_spark_df["NPI"],
            "left"
        ).select(
            joined_df["provider_id"],
            joined_df["provider_name"],
            joined_df["care_site_name"],
            s3_provider_spark_df["Specialty"]
        )

        # Gravacao do dataframe no formato delta
        joined_df.write.format("delta").mode("overwrite").save(config["PROVIDER_CARE_SITE_SILVER"])
        #save_to_parquet(joined_df, "path")
