from fetch import fetch_data
from transform import transform_data
from load_bigquery import load_to_bigquery

raw_data = fetch_data()

if raw_data:

    transformed_df = transform_data(raw_data)

    load_to_bigquery(
        transformed_df
    )