# 🏏 IPL Data Pipeline

An end-to-end data engineering pipeline that extracts IPL match data, transforms it using Python and pandas, loads it into PostgreSQL, and orchestrates the entire workflow using Apache Airflow.

---

## 📌 Project Overview

This project simulates a real-world data engineering pipeline built around the Indian Premier League (IPL) dataset covering matches from 2008 to 2025. The pipeline runs on a daily schedule via Airflow, processes over 278,000 ball-by-ball delivery records, and stores clean, structured data in a PostgreSQL database for analytical querying.

---

## 🏗️ Architecture

```
IPL CSV Data (Kaggle)
        │
        ▼
  Extract (Python)
        │
        ▼
  Transform (pandas)
   - Drop nulls
   - Standardize columns
   - Enrich with derived fields
        │
        ▼
  Load (psycopg2 → PostgreSQL)
        │
        ▼
  Orchestrate (Apache Airflow DAG)
        │
        ▼
  Analytical SQL Queries
```

---

## 🛠️ Tech Stack

| Tool | Purpose |
|---|---|
| Python 3.10 | Core scripting language |
| pandas | Data transformation and cleaning |
| psycopg2 | PostgreSQL database connector |
| PostgreSQL 18 | Data storage |
| Apache Airflow 2.8.1 | Pipeline orchestration |
| SQL | Analytical queries |
| WSL2 (Ubuntu) | Linux environment for Airflow on Windows |

---

## 📁 Project Structure

```
ipl-pipeline/
│
├── dags/
│   └── ipl_pipeline_dag.py      # Airflow DAG definition
│
├── scripts/
│   ├── extract.py               # Load CSVs into DataFrames
│   ├── transform.py             # Clean and enrich data
│   └── load.py                  # Load data into PostgreSQL
│
├── sql/
│   └── insights.sql             # 5 analytical queries
│
├── data/
│   ├── matches_updated_ipl_upto_2025.csv
│   └── deliveries_updated_ipl_upto_2025.csv
│
├── config.py                    # Database and file path configuration
├── requirements.txt             # Python dependencies
└── README.md
```

---

## 📊 Dataset

- **Source:** Kaggle — IPL Ball by Ball Dataset (2008–2025)
- **matches** table: 1,146 rows, 16 columns (after cleaning)
- **deliveries** table: 278,205 rows, 18 columns

---

## ✈️ Airflow DAG

The DAG `ipl_pipeline` runs on a `@daily` schedule with two tasks executing in sequence:

```
extract_transform_load_matches >> extract_transform_load_deliveries
```

- **Task 1** — Extracts, transforms, and loads match data
- **Task 2** — Extracts, transforms, and loads ball-by-ball delivery data

---

## 🔍 Key Insights

Five analytical queries were run on the loaded data to surface meaningful IPL statistics:

**1. Most Successful Team (All-Time Wins)**
| Team | Wins |
|---|---|
| Mumbai Indians | 151 |
| Chennai Super Kings | 142 |
| Kolkata Knight Riders | 135 |

**2. All-Time Leading Run Scorers**
| Batsman | Total Runs |
|---|---|
| V Kohli | 8,671 |
| RG Sharma | 7,048 |
| S Dhawan | 6,769 |

**3. All-Time Leading Wicket Takers**
| Bowler | Wickets |
|---|---|
| YS Chahal | 221 |
| B Kumar | 198 |
| SP Narine | 192 |

**4. Highest Scoring Seasons (Avg Runs Per Match)**
| Season | Avg Match Score |
|---|---|
| 2025 | 366.63 |
| 2024 | 365.79 |
| 2023 | 350.18 |

**5. Most Player of the Match Awards**
| Player | Awards |
|---|---|
| AB de Villiers | 24 |
| CH Gayle | 22 |
| RG Sharma | 21 |

---

## ⚙️ How to Run

### Prerequisites
- Python 3.10+
- PostgreSQL 18
- Apache Airflow 2.8.1
- WSL2 (Ubuntu) — required for Airflow on Windows

### 1. Clone the repository
```bash
git clone https://github.com/your-username/ipl-pipeline.git
cd ipl-pipeline
```

### 2. Install dependencies
```bash
pip install pandas psycopg2-binary sqlalchemy apache-airflow==2.8.1
```

### 3. Configure database
Update `config.py` with your PostgreSQL credentials:
```python
DB_CONFIG = {
    "host": "localhost",
    "database": "ipl_db",
    "user": "postgres",
    "password": "your_password",
    "port": 5432
}
```

### 4. Set up Airflow
```bash
export AIRFLOW_HOME=~/ipl-pipeline/airflow
airflow db init
airflow users create --username admin --password admin \
    --firstname Admin --lastname User --role Admin \
    --email admin@example.com
```

### 5. Start Airflow
```bash
# Terminal 1 — Webserver
airflow webserver --port 8080

# Terminal 2 — Scheduler
airflow scheduler
```

### 6. Trigger the pipeline
Open `http://localhost:8080` → login → trigger `ipl_pipeline` DAG

---

## 🧠 What I Learned

- Building modular ETL pipelines with separation of concerns (extract, transform, load)
- Writing Airflow DAGs and understanding task dependencies
- Debugging cross-environment networking issues (WSL2 ↔ Windows PostgreSQL)
- Data cleaning with pandas — handling nulls, type conversions, column standardization
- Writing analytical SQL queries on real-world sports data

---

## 📬 Contact

**Akhilesh Hiremath**
akhilhiremath7@gmail.com
