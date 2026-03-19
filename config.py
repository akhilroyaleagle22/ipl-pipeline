import os

# Absolute path to project root
BASE_DIR = os.path.expanduser("~/ipl-pipeline")

DB_CONFIG = {
    "host": "172.22.128.1",
    "database": "ipl_db",
    "user": "postgres",
    "password": "your_postgres_password",
    "port": 5432
}

# Absolute file paths
MATCHES_FILE = os.path.join(BASE_DIR, "data/matches_updated_ipl_upto_2025.csv")
DELIVERIES_FILE = os.path.join(BASE_DIR, "data/deliveries_updated_ipl_upto_2025.csv")