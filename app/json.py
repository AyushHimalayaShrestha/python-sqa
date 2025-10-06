# Json Handling
import json

person = {
    "name": "Ayush",
    "age": 27,
    "skills": ["Python", "C#", "Django"]
}

# Write JSON to file
with open("person.json", "w") as file:
    json.dump(person, file, indent=4)

# Read JSON from file
with open("person.json", "r") as file:
    data = json.load(file)

print("Name:", data["name"])
print("Skills:", data["skills"])
