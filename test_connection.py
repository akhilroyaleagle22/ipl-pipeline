from sqlalchemy import create_engine, text
from config import DB_CONFIG

engine = create_engine(
    f"postgresql://{DB_CONFIG['user']}:{DB_CONFIG['password']}"
    f"@{DB_CONFIG['host']}:{DB_CONFIG['port']}/{DB_CONFIG['database']}"   
)

try:
    with engine.connect() as conn:
        result = conn.execute(text("SELECT version();"))
        print("Connected successfully!")
        print(result.fetchone()[0])
except Exception as e:
    print(f" Connection failed: {e}")