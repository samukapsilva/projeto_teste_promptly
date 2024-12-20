from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import timedelta, days_ago

# Importa a função ingest_from_postgres do módulo postgres_ingestion na pasta ingestion
from ingestion.postgres_ingestion_bronze import ingest_from_postgres
# Importa a função ingest_from_s3 do módulo s3_ingestion na pasta ingestion
from ingestion.s3_ingestion_bronze import ingest_from_s3
# Importa o Spark para lidar com o data transformation
from transformation.transform_spark import *
# Adicionado para lidar com o config.properties
import configparser


config = configparser.ConfigParser()
config.read("config.properties")


default_args = {
    'owner': 'admin',
    'depends_on_past': False,
    'retries': 3,
    'retry_delay': timedelta(minutes=5),
}

with DAG(
    'data_pipeline',
    default_args=default_args,
    description='Pipeline de harmonização de dados',
    schedule_interval='@daily',
    start_date=days_ago(1),
) as dag:

    ingest_postgres = PythonOperator(
        task_id='ingest_postgres',
        python_callable=ingest_from_postgres,
    )

    ingest_s3 = PythonOperator(
        task_id='ingest_s3',
        python_callable=lambda: ingest_from_s3(config["BUCKET_NAME"]'', config["S3_PROVIDER"] + '.csv'),
    )

    transform = PythonOperator(
        task_id='transform',
        python_callable=transform_spark_silver,
    )

    ingest_postgres >> ingest_s3 >> transform_spark_silver


