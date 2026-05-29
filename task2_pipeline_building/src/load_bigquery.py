from google.cloud import bigquery
from config import (
    PROJECT_ID,
    DATASET_ID,
    TABLE_ID
)

def load_to_bigquery(df):

    client = bigquery.Client(
        project=PROJECT_ID
    )

    table_ref = \
        f"{PROJECT_ID}.{DATASET_ID}.{TABLE_ID}"

    job = client.load_table_from_dataframe(
        df,
        table_ref
    )

    job.result()

    print("Data loaded successfully.")