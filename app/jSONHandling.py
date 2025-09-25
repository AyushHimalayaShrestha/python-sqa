# JSON Handling (Save & Load)
import json

data = {"name": "Ayush", "age": 28, "skills": ["Python", "Django", "SQL", "C#"]}

# Save to JSON file
with open("data.json", "w") as f:
    json.dump(data, f)

# Load from JSON file
with open("data.json", "r") as f:
    loaded = json.load(f)

print("Loaded JSON:", loaded)
