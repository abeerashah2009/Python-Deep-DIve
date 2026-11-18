# Lab 40 - Final Mini-Project: Building a CLI Data Processor

## 1. Introduction

In this lab, I created a Command-Line Interface (CLI) Data Processor using Python.

The program collects JSON data from an online API or a local JSON file, validates the data, and saves it into another JSON file.

## 2. Objectives

- Learn how to fetch data from an API.
- Understand how to read local JSON files.
- Use Python Requests to make HTTP requests.
- Save data into JSON files.
- Understand command-line arguments using argparse.
- Apply JSON validation.
- Use logging to display program information.
- Handle errors using try and except.

## 3. Technologies Used

- Python 3.12.3
- Requests 2.32.3
- Ubuntu 24.04
- Linux Terminal
- JSON
- argparse
- logging

## 4. Project Setup

First, I cloned my Python repository and created a separate project directory.

```bash
git clone https://github.com/abeerashah2009/Python-Deep-DIve.git
mkdir -p ~/data-processor
cd ~/data-processor
```

Created and activated a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Installed the required Requests library:

```bash
pip install requests==2.32.3
```

## 5. Python Libraries

The project uses the following libraries:

- **argparse:** Accepts command-line arguments.
- **json:** Reads and writes JSON data.
- **logging:** Displays application information and errors.
- **sys:** Handles program exit codes.
- **requests:** Sends HTTP requests and fetches API data.

## 6. Main Functions

### fetch_data(source)

This function fetches JSON data from:
- HTTP or HTTPS API URLs.
- Local JSON file paths.
- file:// URLs.

### save_data_to_file(data, file_path)

This function saves the fetched data into a JSON file using `json.dump()`.

### parse_arguments()

This function uses argparse to accept:
- `--url`: API URL or local file path.
- `--out`: Output JSON file path.

### validate(data)

This function checks that the JSON data is a list containing dictionaries.

### main()

The main function connects all the project components:
- Reads command-line arguments.
- Fetches JSON data.
- Validates the data.
- Saves the output.
- Handles errors and returns an exit code.

## 7. Running the Program

### Fetch data from an API

```bash
python3 data_processor.py \
  --url https://jsonplaceholder.typicode.com/posts \
  --out posts.json
```

### Read a local JSON file

```bash
python3 data_processor.py --url sample.json --out local.json
```

### Read using file:// URL

```bash
python3 data_processor.py --url file://$PWD/sample.json --out local2.json
```

## 8. Logging

Logging helps monitor program activity.

The program displays:
- INFO messages when fetching data.
- INFO messages when data is validated.
- INFO messages when data is saved.
- ERROR messages when an operation fails.

## 9. Error Handling

The program handles the following errors:

- Network request errors.
- File and operating system errors.
- Invalid JSON structure.

If an error occurs, the program displays an error message and returns exit code `1`.

## 10. Practical Testing and Results

| Test | Result |
|---|---|
| Python syntax check | PASS |
| Live API request | PASS |
| Live API records | 100 |
| JSON output validation | PASS |
| Local file input | PASS |
| file:// URL input | PASS |
| Invalid URL handling | PASS |
| Invalid JSON structure | PASS |
| Error exit code | 1 |
| Unwanted output prevention | PASS |

## 11. Important Commands

Check Python version:

```bash
python3 --version
```

Check Requests version:

```bash
pip show requests
```

Check Python syntax:

```bash
python3 -m py_compile data_processor.py
```

Display CLI help:

```bash
python3 data_processor.py --help
```

Validate JSON:

```bash
python3 -m json.tool posts.json
```

## 12. What I Learned

After completing this lab, I learned how to:

- Build a Python command-line application.
- Fetch data from an online API.
- Work with JSON files.
- Use argparse for command-line input.
- Validate data before saving it.
- Apply logging and exception handling.
- Test successful and unsuccessful operations.

## 13. Lab Result

**LMS Score: 100 / 100**

**Status: PASSED**

This project helped me understand how to build a practical Python CLI application for processing JSON data.
