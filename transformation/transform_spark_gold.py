from pyspark.sql import SparkSession
from pyspark.sql.functions import col
from utils.utils import *

class SparkDataTransformer:
    def __init__(self):
        # Inicializa o SparkSession
       builder = SparkSession.builder \
            .appName("SparkDataTransformerSilver") \
            .config("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension") \
            .config("spark.sql.catalog.spark_catalog", "org.apache.spark.sql.delta.catalog.DeltaCatalog") \
            .getOrCreate()

        self.spark = configure_spark_with_delta_pip(builder).getOrCreate()


        # Converte os pandas DataFrames para Spark DataFrames
        provider_care_site_silver_df   =  spark.read.parquet(config["PROVIDER_CARE_SITE_SILVER"])


        # regras de agregação, refinamento, etc...
        

        # Gravacao do dataframe final, refinado em formado delta
        joined_df.write.format("delta").mode("overwrite").save(config["PROVIDER_CARE_SITE_SILVER"])
