from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import sys
import os

# Add project root to path so Airflow can find our scripts
sys.path.insert(0, os.path.expanduser("~/ipl-pipeline"))

from scripts.extract import extract_matches, extract_deliveries
from scripts.transform import transform_matches, transform_deliveries
from scripts.load import load_to_postgres

# ── Task functions ──────────────────────────────────────────

def run_extract_transform_load_matches():
    df = extract_matches()
    df = transform_matches(df)
    load_to_postgres(df, "matches")

def run_extract_transform_load_deliveries():
    df = extract_deliveries()
    df = transform_deliveries(df)
    load_to_postgres(df, "deliveries")

# ── DAG definition ──────────────────────────────────────────

with DAG(
    dag_id="ipl_pipeline",
    start_date=datetime(2024, 1, 1),
    schedule_interval="@daily",
    catchup=False,
    tags=["ipl", "portfolio"],
    description="IPL data pipeline — extract, transform, load into PostgreSQL",
) as dag:

    matches_task = PythonOperator(
        task_id="extract_transform_load_matches",
        python_callable=run_extract_transform_load_matches,
    )

    deliveries_task = PythonOperator(
        task_id="extract_transform_load_deliveries",
        python_callable=run_extract_transform_load_deliveries,
    )

    # Matches must load before deliveries
    matches_task >> deliveries_task