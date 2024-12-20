import psycopg2
import pandas as pd
from utils.utils import save_to_parquet
import config.properties

def ingest_from_postgres(table_name):
    try:
        conn = psycopg2.connect(
            host="localhost",
            database="database",
            user="user",
            password="password"
        )
        table = f"SELECT * FROM {table_name};"
        table_df = pd.read_sql(table, conn)
        table_df['_timestamp'] = pd.Timestamp.now()
        
        save_to_parquet(table_df, "path")

    except Exception as e:
        print(f"Erro ao extrair dados da tabela '{table_name}': {e}")
    
    finally:
        conn.close()
    # return table_df











    