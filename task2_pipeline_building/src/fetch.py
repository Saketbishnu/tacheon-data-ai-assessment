import requests
import logging
from task2_pipeline_building.src.config import API_URL, PARAMS

logging.basicConfig(level=logging.INFO)

def fetch_data():

    try:

        logging.info("Calling CoinGecko API...")

        response = requests.get(
            API_URL,
            params=PARAMS,
            timeout=10
        )

        response.raise_for_status()

        data = response.json()

        logging.info(
            f"Successfully fetched {len(data)} records."
        )

        return data

    except requests.exceptions.RequestException as e:

        logging.error(
            f"API request failed: {e}"
        )

        return []