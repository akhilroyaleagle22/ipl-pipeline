from sqlalchemy import create_engine
from config import DB_CONFIG

def get_engine():
    url = (
        f"postgresql://{DB_CONFIG['user']}:{DB_CONFIG['password']}"
        f"@{DB_CONFIG['host']}:{DB_CONFIG['port']}/{DB_CONFIG['database']}"
    )
    return create_engine(url)

def load_to_postgres(df, table_name):
    engine = get_engine()
    df.to_sql(
        table_name,
        engine,
        if_exists="replace",
        index=False,
        chunksize=1000
    )
    print(f"✅ Loaded {len(df)} rows into table '{table_name}'")