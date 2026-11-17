import json

# Create a Python dictionary
employee_data = {
    "name": "John Doe",
    "age": 30,
    "department": "Engineering",
    "skills": ["Python", "Django", "Machine Learning"]
}

print(type(employee_data))
# Convert the dictionary to a JSON string
employee_data_json = json.dumps(employee_data, indent=4)

print(type(employee_data_json))
print(employee_data_json)
# Write JSON data to a file
with open("employee_data.json", "w", encoding="utf-8") as f:
    json.dump(employee_data, f, indent=4)
# Read JSON data from the file
with open("employee_data.json", "r", encoding="utf-8") as f:
    data = json.load(f)

print(data)

# Convert JSON string back to Python dictionary
data_from_string = json.loads(employee_data_json)

# Verify that the original and loaded data match
assert data == employee_data
assert data_from_string == employee_data

print("Round trip OK")
