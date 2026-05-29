SELECT
    name,
    current_price,
    market_cap,
    ROUND(volume_marketcap_ratio,4)
        AS volume_ratio
FROM
`mercurial-ruler-463410-p3.crypto_dataset.market_data`
ORDER BY market_cap DESC
LIMIT 5;