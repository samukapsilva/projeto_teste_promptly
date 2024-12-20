from pyspark.sql import SparkSession
import pandas as pd

def save_to_parquet(df, output_path):
    df.to_parquet(output_path, index=False)


def pandas_to_spark(self, pandas_df):
    # Converte um df Pandas para um df park.
    return self.spark.createDataFrame(pandas_df)