# Importa a função ingest_from_postgres do módulo postgres_ingestion na pasta ingestion
from ingestion.postgres_ingestion import ingest_from_postgres
# Importa a função ingest_from_s3 do módulo s3_ingestion na pasta ingestion
from ingestion.s3_ingestion import ingest_from_s3
# Importa funções uteis
from utils.utils import *
# Adicionado para lidar com o config.properties
import configparser
# Adicionado para lidar com a transformation
from transformation.transform_spark import *
# Adicionado a lib para criar uma arquitetura de logs
import logging

# Configuração do logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

config = configparser.ConfigParser()
config.read("config.properties")

# Main Function
if __name__ == "__main__":

    # Ingest  
    logger.info(f"Iniciando a ingestão dos dados da tabela '{config["POSTGRES_PROVIDER"]}'")
    ingest_from_postgres(config["POSTGRES_PROVIDER"])

    logger.info(f"Iniciando a ingestão dos dados da tabela '{config["POSTGRES_CARE_SITE"]}'")
    ingest_from_postgres(config["POSTGRES_CARE_SITE"])

    logger.info(f"Iniciando a ingestão dos dados da tabela '{config["S3_PROVIDER"]}'")
    ingest_from_s3(config["S3_PROVIDER"])

    # Transform / Load
    logger.info("Iniciando a transformacao e load dos dados extraidos nas tabelas bronze")
    spark = SparkDataTransformer()