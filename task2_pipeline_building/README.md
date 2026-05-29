# Task 2 — Building a Data Pipeline using CoinGecko API

## Project Overview

In this project, I built a simple end-to-end data pipeline using the CoinGecko public API. The main goal was to automate the process of collecting cryptocurrency market data, transforming it into a cleaner analytical format, and storing it in Google BigQuery for further analysis.

I selected CoinGecko because it provides publicly accessible cryptocurrency data without requiring authentication, making it convenient for learning API integration and data engineering concepts.

---

## Pipeline Architecture

The workflow of the pipeline follows these steps:

**CoinGecko API → Data Extraction → Data Transformation → BigQuery Storage → SQL Analysis**

The pipeline starts by fetching live market data from the CoinGecko API. After extraction, the raw data is cleaned and transformed before being uploaded into BigQuery, where SQL queries can be used for analysis.

---

## Project Structure

### 1. `fetch.py`

This module handles communication with the CoinGecko API.

Its responsibilities include:

* Sending API requests
* Managing response validation
* Handling request failures and exceptions
* Generating logs for debugging and monitoring

---

### 2. `transform.py`

This file is responsible for preparing the raw API data for analytics.

The transformation process includes:

* Cleaning unnecessary or inconsistent data
* Handling missing or null values
* Performing datatype conversions
* Creating derived analytical metrics

One additional metric implemented in this project is:

**`volume_marketcap_ratio`**

This metric helps measure trading activity relative to a cryptocurrency’s market capitalization, providing a better understanding of market behavior.

---

### 3. `load_bigquery.py`

This module manages the connection between the pipeline and Google BigQuery.

Its tasks include:

* Establishing the BigQuery client connection
* Preparing the dataset and table structure
* Uploading transformed data into BigQuery tables

---

### 4. `main.py`

This file acts as the orchestration layer of the pipeline.

It coordinates the overall workflow by executing the extraction, transformation, and loading stages in the correct sequence.

---

## BigQuery Configuration

The processed data is stored in Google BigQuery using the following setup:

**Project ID:** `mercurial-ruler-463410-p3`
**Dataset:** `crypto_dataset`
**Table:** `market_data`

---

## Running the Pipeline

To run the project locally, first install the required dependencies:

```bash
pip install -r requirements.txt
```

After installation, execute the pipeline using:

```bash
python src/main.py
```

---

## SQL Analytics

After loading the data into BigQuery, SQL queries can be used for analysis.

The SQL queries for this task are available in:

`sql/summary_query.sql`

An example query included in the project retrieves the top cryptocurrencies ranked by market capitalization.

---

## Production Considerations

Although this project is designed as a learning implementation, several improvements could make it production-ready.

### Automatic Scheduling

In a real-world environment, the pipeline could run automatically using tools such as:

* Cloud Scheduler
* Apache Airflow
* Cron Jobs
* GitHub Actions

### Failure Monitoring

To improve reliability, production monitoring could include:

* Structured logging
* Retry mechanisms for failed API calls
* Alert notifications
* Health monitoring dashboards

### Scaling for Larger Data Volumes

If the amount of incoming data increased significantly, the pipeline could be optimized through:

* Batch data processing
* Incremental loading strategies
* Partitioned BigQuery tables
* Parallel API requests
* Workflow orchestration systems

Overall, this project demonstrates the core concepts of building a practical ETL/ELT style data pipeline using APIs, Python, and cloud-based analytical storage.
