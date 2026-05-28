API_URL = "https://api.coingecko.com/api/v3/coins/markets"

PARAMS = {
    "vs_currency": "usd",
    "order": "market_cap_desc",
    "per_page": 10,
    "page": 1
}

PROJECT_ID = "YOUR_BIGQUERY_PROJECT_ID"

DATASET_ID = "crypto_dataset"

TABLE_ID = "market_data"