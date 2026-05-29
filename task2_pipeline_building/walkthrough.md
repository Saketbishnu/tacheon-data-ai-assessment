# Walkthrough

My goal was to build a simple but production-oriented pipeline.

I selected CoinGecko because it provides structured public data without authentication complexity.

The pipeline was divided into modular components:

* Extraction
* Transformation
* Storage

Transformation included null handling, type normalization, and a derived analytical field.

BigQuery was selected as required by the assignment.

For production readiness, I considered scheduling, monitoring, and scalability rather than limiting the solution to a local script.

With additional time, I would explore:

* incremental ingestion
* historical snapshot storage
* automated testing
* containerized deployment
