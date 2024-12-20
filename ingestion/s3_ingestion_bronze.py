import boto3
import pandas as pd
from utils.utils import save_to_parquet

def ingest_from_s3(bucket_name, file_key):
    try:
        s3 = boto3.client('s3', endpoint_url='http://localhost:9000', aws_access_key_id='s3admin', aws_secret_access_key='s3admin')
        obj = s3.get_object(Bucket=bucket_name, Key=file_key)
        data_df = pd.read_csv(obj['Body'])
        data_df['_timestamp'] = pd.Timestamp.now()
        
        save_to_parquet(data_df, "path")
    except Exception as e:
        print(f"Erro ao tentar ingerir o dataframe")
    #return data_df
