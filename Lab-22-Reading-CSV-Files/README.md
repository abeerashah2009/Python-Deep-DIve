# Lab 22: Reading CSV Files in Python

## 1. Objectives

- Understand CSV (Comma-Separated Values) files.
- Import and use Python's built-in `csv` module.
- Open and read CSV files using `open()`.
- Read rows using `csv.reader()`.
- Handle CSV files with and without headers.
- Store CSV records in a list of dictionaries using `csv.DictReader()`.

---

## 2. Introduction to CSV Files

CSV stands for **Comma-Separated Values**.

A CSV file stores data in a table-like format. Each line represents a record, and commas separate the individual values.

Example:

```csv
id,name,city,score
1,Alice,Karachi,88
2,Bob,Lahore,92
3,Carol,Islamabad,75
```

CSV files are commonly used to store and exchange data between applications, spreadsheets, and data analysis tools.

## 3. Python CSV Module

Python provides a built-in module called `csv` for reading and writing CSV files.

Import it using:

```python
import csv
```

The CSV module does not require a separate pip installation.

**Important functions:**

| Function | Purpose |
|---|---|
| `csv.reader()` | Reads CSV rows as lists |
| `csv.DictReader()` | Reads CSV rows as dictionaries |
| `next()` | Gets the next row from an iterator |
| `open()` | Opens a file |

## 4. Lab Environment Setup

Operating system: Ubuntu 24.04

Python version: 3.12.3

Install Python and the virtual environment module:

```bash
sudo apt update
sudo apt install -y python3 python3-venv
```

Create a working directory:

```bash
mkdir -p ~/csv-lab
cd ~/csv-lab
```

Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
python3 --version
```

Expected version:

```text
Python 3.12.3
```

## 5. Creating a Sample CSV File

Create `sample.csv`:

```csv
id,name,city,score
1,Alice,Karachi,88
2,Bob,Lahore,92
3,Carol,Islamabad,75
4,Dave,Peshawar,81
5,Eve,Quetta,95
```

The file contains:
- One header row.
- Five data records.
- Four columns: id, name, city, and score.

View the file:

```bash
cat sample.csv
```

## 6. Task 2: Importing the CSV Module

Import the CSV module:

```python
import csv
```

The module provides tools for handling CSV data in Python.

## 7. Task 3: Opening a CSV File

Python uses the built-in `open()` function to access files.

Example:

```python
import csv

file_path = 'sample.csv'

with open(file_path, mode='r', newline='') as file:
    print('Opened:', file.name)
```

Expected output:

```text
Opened: sample.csv
```

**Explanation:**

- `open()` opens the file.
- `mode='r'` means read mode.
- `newline=''` allows the CSV module to handle line endings correctly.
- `with` automatically closes the file after use.
- `file.name` displays the file name.

## 8. Task 4: Reading CSV File Content

Use `csv.reader()` to read CSV rows.

Example:

```python
import csv

file_path = 'sample.csv'

with open(file_path, mode='r', newline='') as file:
    csv_reader = csv.reader(file)

    for row in csv_reader:
        print(row)
```

Expected output:

```text
['id', 'name', 'city', 'score']
['1', 'Alice', 'Karachi', '88']
['2', 'Bob', 'Lahore', '92']
['3', 'Carol', 'Islamabad', '75']
['4', 'Dave', 'Peshawar', '81']
['5', 'Eve', 'Quetta', '95']
```

**Explanation:**

- `csv.reader(file)` creates a CSV reader.
- The `for` loop reads each row.
- Every row is returned as a list.
- CSV values are read as strings.

## 9. Task 5: Handling CSV Headers

### Case 1: CSV File With Headers

Use `next()` to read the header separately and then process the remaining records.

```python
import csv

file_path = 'sample.csv'

with open(file_path, mode='r', newline='') as file:
    csv_reader = csv.reader(file)
    header = next(csv_reader)

    print('Header:', header)

    for row in csv_reader:
        print(row)
```

Expected output:

```text
Header: ['id', 'name', 'city', 'score']
['1', 'Alice', 'Karachi', '88']
['2', 'Bob', 'Lahore', '92']
['3', 'Carol', 'Islamabad', '75']
['4', 'Dave', 'Peshawar', '81']
['5', 'Eve', 'Quetta', '95']
```

### Case 2: CSV File Without Headers

Create a headerless CSV file:

```bash
tail -n +2 sample.csv > noheader.csv
```

Python program (`read_noheader.py`):

```python
import csv

with open('noheader.csv', mode='r', newline='') as file:
    csv_reader = csv.reader(file)

    for row in csv_reader:
        print(row)
```

Expected output:

```text
['1', 'Alice', 'Karachi', '88']
['2', 'Bob', 'Lahore', '92']
['3', 'Carol', 'Islamabad', '75']
['4', 'Dave', 'Peshawar', '81']
['5', 'Eve', 'Quetta', '95']
```

**Key point:** A headerless CSV file can be read directly using `csv.reader()`.

## 10. Task 6: Storing CSV Data in a List of Dictionaries

`csv.DictReader()` reads each CSV record as a dictionary.

The header names become dictionary keys.

Program (`read_csv.py`):

```python
import csv

file_path = 'sample.csv'
data_list = []

with open(file_path, mode='r', newline='') as file:
    csv_reader = csv.DictReader(file)

    for row in csv_reader:
        data_list.append(row)

# Print the list of dictionaries
for item in data_list:
    print(item)

print('Records:', len(data_list))
```

Expected output:

```text
{'id': '1', 'name': 'Alice', 'city': 'Karachi', 'score': '88'}
{'id': '2', 'name': 'Bob', 'city': 'Lahore', 'score': '92'}
{'id': '3', 'name': 'Carol', 'city': 'Islamabad', 'score': '75'}
{'id': '4', 'name': 'Dave', 'city': 'Peshawar', 'score': '81'}
{'id': '5', 'name': 'Eve', 'city': 'Quetta', 'score': '95'}
Records: 5
```

**Explanation:**

- `data_list = []` creates an empty list.
- `csv.DictReader(file)` reads each record as a dictionary.
- `data_list.append(row)` adds each dictionary to the list.
- `len(data_list)` counts the records.

Example dictionary:

```python
{
    'id': '1',
    'name': 'Alice',
    'city': 'Karachi',
    'score': '88'
}
```

The column names are keys, and the corresponding row values are values.

## 11. Verifying the Number of Records

Use the Linux `wc -l` command to count CSV lines:

```bash
wc -l < sample.csv
```

Expected output:

```text
6
```

Calculation:

```text
Total lines = 6
Header lines = 1
Data records = 6 - 1 = 5
```

The Python program also displays:

```text
Records: 5
```

Both results match.

## 12. Important Differences

| Feature | `csv.reader()` | `csv.DictReader()` |
|---|---|---|
| Data format | List | Dictionary |
| Header handling | Manual | Uses header as keys |
| Access | By index | By column name |
| Best use | Simple row reading | Structured data |

Example:

```python
# csv.reader()
row[1]

# csv.DictReader()
row['name']
```

## 13. Verification and Testing

The following checks were completed:

- Python 3.12.3 verified.
- Virtual environment created and activated.
- Sample CSV file created with one header and five records.
- CSV module imported successfully.
- CSV file opened successfully.
- `csv.reader()` read all rows.
- Header row handled using `next()`.
- Headerless CSV file read successfully.
- `csv.DictReader()` created dictionaries.
- Five records counted successfully.
- CSV line count verified as six.
- Python syntax compilation passed.

## 14. Evidence Files

The evidence directory contains:

| Evidence file | Purpose |
|---|---|
| `python-version.txt` | Python version |
| `compile-check.txt` | Python syntax check |
| `code-structure.txt` | Important code statements |
| `dictionary-output.txt` | Dictionary output |
| `headerless-output.txt` | Headerless CSV output |
| `csv-line-count.txt` | CSV line count |

## 15. Interview Questions and Answers

**Q1. What is a CSV file?**

CSV stands for Comma-Separated Values. It stores data in rows and columns using commas as separators.

**Q2. What is the Python CSV module?**

It is a built-in Python module used to read and write CSV files.

**Q3. Do we need to install the CSV module?**

No. It is included in Python's standard library.

**Q4. What does `csv.reader()` do?**

It reads CSV data row by row and returns each row as a list of strings.

**Q5. What does `csv.DictReader()` do?**

It reads CSV records as dictionaries using the header names as keys.

**Q6. What is the purpose of `newline=''`?**

It allows the CSV module to handle newline characters correctly.

**Q7. Why do we use `next()`?**

It retrieves the next item from an iterator. In this lab, it is used to read the header separately.

**Q8. What is a header row?**

A header row contains column names, such as `id`, `name`, `city`, and `score`.

**Q9. What is the difference between `csv.reader()` and `csv.DictReader()`?**

`csv.reader()` returns lists, while `csv.DictReader()` returns dictionaries.

**Q10. Why do we use `data_list.append(row)`?**

It adds each dictionary record to the list.

**Q11. How can we count the records in a CSV file?**

We can use Python's `len(data_list)` or count file lines and subtract the header line.

**Q12. What is a virtual environment?**

A virtual environment provides an isolated Python environment for a project.

## 16. Conclusion

In this lab, I learned how to read CSV files using Python's built-in `csv` module. I practiced importing the module, opening files, reading rows, handling CSV headers, and storing records in a list of dictionaries.

I also verified the program output, Python syntax, and CSV record count.

These skills are useful in Python automation, data processing, and data analysis projects.

**Lab 22: Reading CSV Files — Completed.**
