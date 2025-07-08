# Write to JSON file
with open("recent.json", "w") as f:
    json.dump(recent_data, f)

# Later, read from same file
with open("recent.json", "r") as f:
    recent_data = json.load(f)
