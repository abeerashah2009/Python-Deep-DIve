# Lab 14: JSON Handling

## 1. Overview

This lab demonstrates how to work with JSON (JavaScript Object Notation) in Python.

JSON is a lightweight data format used to store and exchange information between applications.

Python provides a built-in `json` module for handling JSON data.

## 2. Objectives

- Create a Python dictionary.
- Convert a Python dictionary into a JSON string.
- Write JSON data into a file.
- Read JSON data from a file.
- Convert JSON strings back into Python objects.
- Use JSON files for application configuration.
- Handle invalid JSON using exception handling.

## 3. Lab Environment

| Item | Details |
|---|---|
| Operating System | Ubuntu 24.04 |
| Python Version | 3.12.3 |
| JSON Module | Python built-in `json` |
| Editor | Nano |
| Repository | Python-Deep-DIve |

No external Python package was required.

## 4. Introduction to JSON

JSON stands for JavaScript Object Notation.

It is commonly used for:

- Application configuration.
- Data exchange between applications.
- Web APIs.
- Storing structured information.

Example JSON:

```json
{
    "name": "John Doe",
    "age": 30,
    "department": "Engineering"
}
```

## 5. Task 1: Creating a Python Dictionary

The first step was to create an employee dictionary.

File: `json_lab.py`

```python
import json

employee_data = {
    "name": "John Doe",
    "age": 30,
    "department": "Engineering",
    "skills": ["Python", "Django", "Machine Learning"]
}

print(type(employee_data))
```

Output:

```text
<class 'dict'>
```

The output confirms that the data is a Python dictionary.

## 6. Converting a Dictionary into JSON

Python provides `json.dumps()` to convert a Python object into a JSON string.

```python
employee_data_json = json.dumps(employee_data, indent=4)

print(type(employee_data_json))
print(employee_data_json)
```

Output:

```text
<class 'str'>
```

The JSON string contains the employee information in readable format.

The `indent=4` option formats the JSON with four spaces.

## 7. Task 2: Writing JSON Data into a File

The `json.dump()` function writes Python data into a JSON file.

```python
with open("employee_data.json", "w", encoding="utf-8") as f:
    json.dump(employee_data, f, indent=4)
```

The generated file is:

`employee_data.json`

The file stores employee information in JSON format.

## 8. Reading JSON Data from a File

The `json.load()` function reads JSON data from a file.

```python
with open("employee_data.json", "r", encoding="utf-8") as f:
    data = json.load(f)

print(data)
```

The JSON file is read and converted into a Python dictionary.

## 9. JSON String Conversion and Round-Trip Verification

The `json.loads()` function converts a JSON string back into a Python object.

```python
data_from_string = json.loads(employee_data_json)

assert data == employee_data
assert data_from_string == employee_data

print("Round trip OK")
```

Output:

```text
Round trip OK
```

This confirms that the original and converted data match.

## 10. Difference Between JSON Functions

| Function | Purpose |
|---|---|
| `json.dump()` | Writes Python data to a JSON file |
| `json.dumps()` | Converts Python data into a JSON string |
| `json.load()` | Reads JSON data from a file |
| `json.loads()` | Converts a JSON string into Python data |

Remember:

- Functions without `s` (`dump`, `load`) work with files.
- Functions with `s` (`dumps`, `loads`) work with strings.

## 11. Task 3: JSON Configuration File

A JSON file can store application configuration settings.

File: `config.json`

```json
{
    "port": 9090
}
```

The application uses port `9090`.

## 12. Loading Configuration with Default Values

File: `config_loader.py`

```python
import json

DEFAULTS = {
    "host": "localhost",
    "port": 8080,
    "debug": False
}


def load_config(path):
    try:
        with open(path, "r", encoding="utf-8") as f:
            return {**DEFAULTS, **json.load(f)}

    except json.JSONDecodeError as e:
        print(f"Invalid JSON in {path}: {e}")
        return DEFAULTS


print(load_config("config.json"))
print(load_config("broken.json"))
```

The program combines default settings with the values from the configuration file.

The valid configuration overrides the default port.

## 13. Handling Invalid JSON

A deliberately invalid file named `broken.json` was created.

```json
{"port": 9090,}
```

The trailing comma makes this JSON invalid.

Python raises `json.JSONDecodeError` when it tries to parse the file.

The `try` and `except` blocks handle this error and return the default configuration.

Output:

```text
{'host': 'localhost', 'port': 9090, 'debug': False}
Invalid JSON in broken.json: Expecting property name enclosed in double quotes: line 1 column 15 (char 14)
{'host': 'localhost', 'port': 8080, 'debug': False}
```

## 14. JSON Validation

The following command checks whether a JSON file is valid:

```bash
python3 -m json.tool employee_data.json
```

Validation results:

```text
employee_data.json: VALID
config.json: VALID
```

The `broken.json` file is intentionally invalid and is used for exception-handling practice.

## 15. Python Syntax Validation

The following command checks Python syntax:

```bash
python3 -m py_compile json_lab.py config_loader.py
```

Result:

```text
Python syntax check: PASSED
```

Both Python scripts passed syntax compilation.

## 16. Project Structure

```text
Lab-14-JSON-Handling/
├── README.md
├── json_lab.py
├── employee_data.json
├── config.json
├── config_loader.py
├── broken.json
└── evidence/
    ├── python-version.txt
    ├── task1-output.txt
    ├── task2-output.txt
    ├── json-file-details.txt
    ├── json-name-check.txt
    ├── json-tool-output.txt
    ├── config-loader-output.txt
    └── syntax-check.txt
```

## 17. Evidence and Verification

The `evidence/` directory contains:

- Python version information.
- Dictionary and JSON string output.
- JSON file details.
- JSON reading and round-trip output.
- Employee name verification.
- JSON formatting output.
- Configuration loader output.
- Python syntax validation result.

These files provide proof of the practical tasks and their verification.

## 18. Conclusion

In this lab, I learned how to handle JSON data using Python.

I practiced creating dictionaries, converting data into JSON strings, writing and reading JSON files, and using JSON for application configuration.

I also learned how to handle invalid JSON using `json.JSONDecodeError`.

All practical tasks were executed and verified successfully.
