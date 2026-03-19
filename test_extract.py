from scripts.extract import extract_matches, extract_deliveries

matches = extract_matches()
deliveries = extract_deliveries()

print("\n--- Matches Columns ---")
print(matches.columns.tolist())

print("\n--- Matches Sample ---")
print(matches.head(3))

print("\n--- Deliveries Columns ---")
print(deliveries.columns.tolist())

print("\n--- Deliveries Sample ---")
print(deliveries.head(3))
