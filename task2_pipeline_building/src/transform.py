import pandas as pd

def transform_data(raw_data):

    df = pd.DataFrame(raw_data)

    selected_columns = [

        "id",
        "symbol",
        "name",
        "current_price",
        "market_cap",
        "total_volume",
        "price_change_percentage_24h"

    ]

    df = df[selected_columns]

    df.fillna(0, inplace=True)

    df["current_price"] = \
        pd.to_numeric(
            df["current_price"],
            errors="coerce"
        )

    df["market_cap"] = \
        pd.to_numeric(
            df["market_cap"],
            errors="coerce"
        )

    df["volume_marketcap_ratio"] = \
        df["total_volume"] / df["market_cap"]

    return df