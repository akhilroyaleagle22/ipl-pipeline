import pandas as pd
from config import MATCHES_FILE, DELIVERIES_FILE

def extract_matches():
    df = pd.read_csv(MATCHES_FILE)
    print(f"Extracted matches: {len(df)} rows, {len(df.columns)} columns")
    return df

def extract_deliveries():
    df = pd.read_csv(DELIVERIES_FILE)
    print(f"Extracted deliveries: {len(df)} roes, {len(df.columns)} columns")
    return df
