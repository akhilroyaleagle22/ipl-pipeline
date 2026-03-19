from scripts.extract import extract_matches, extract_deliveries
from scripts.transform import transform_matches, transform_deliveries
from scripts.load import load_to_postgres

# Extract
matches = extract_matches()
deliveries = extract_deliveries()

# Transform
matches_clean = transform_matches(matches)
deliveries_clean = transform_deliveries(deliveries)

# Load into PostgreSQL
print("\nLoading into PostgreSQL...")
load_to_postgres(matches_clean, "matches")
load_to_postgres(deliveries_clean, "deliveries")

print("\n🎉 Pipeline complete!")