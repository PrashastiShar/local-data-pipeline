# Containerized Data Analytics Pipeline (DuckDB & Docker)

A data engineering project demonstrating how to process large-scale, real-world datasets inside an isolated, reproducible cloud-native environment.

## 📌 Project Overview
This pipeline downloads a massive real-world dataset (over 300,000 rows of global COVID-19 data) and uses **DuckDB** to run complex SQL aggregations directly on the raw CSV file. 

By utilizing DuckDB, the pipeline achieves **sub-second query execution times** without needing to load the entire dataset into memory or set up a heavy database server. The entire environment is containerized using **Docker** to guarantee reproducibility across any operating system.

## ⚙️ How It Works
1. **Data Ingestion:** The Python script automatically downloads the latest COVID-19 dataset from a remote URL.
2. **Serverless SQL Querying:** DuckDB queries the CSV file directly in-memory, grouping by location and calculating maximum death and vaccination counts.
3. **Containerization:** The script and its dependencies (Pandas, DuckDB, Requests) are packaged into a Docker container.

## 🛠️ Tech Stack
*   **Language:** Python
*   **Data Engine:** DuckDB
*   **Containerization:** Docker

## 🚀 How to Run
1. Build the Docker image:
   ```bash
   docker build -t local-data-pipeline .

2. Run the pipeline:
docker run local-data-pipeline
📊 Benchmark Results
Dataset Size: 300,000+ rows

Query Execution Time: ~0.39 seconds

Environment: Dockerized Python 3.10 (slim)
