from scripts.extract import extract_matches, extract_deliveries
from scripts.transform import transform_matches, transform_deliveries

#Extract
matches = extract_matches()
deliveries = extract_deliveries()

#Transform
matches_clean = transform_matches(matches)
deliveries_clean = transform_deliveries(deliveries)

#check results
print("\n--- Cleaned matches sample ---")
print(matches_clean.head(3))
print("\n--- Cleaned matches columns ---")
print(matches_clean.columns.tolist())

print("\n--- Cleaned deliveries sample ---")
print(deliveries_clean.head(3))
print("\n--- Null check Matches ---")
print(matches_clean.isnull().sum())