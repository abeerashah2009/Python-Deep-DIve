# Lab 30 - Basic SQLite Usage

## Objective
Learn how to use SQLite with Python to create databases, create tables, insert records, retrieve data, and verify database contents.

## Tools and Environment
- Ubuntu 24.04
- Python 3.12
- SQLite 3
- Python `sqlite3` module

## Tasks Completed

### 1. Import SQLite
Imported Python's built-in `sqlite3` module.

### 2. Create an In-Memory Database
Connected to SQLite using `:memory:`.

### 3. Create a Students Table
Created a `students` table with:
- `id` - INTEGER PRIMARY KEY
- `name` - TEXT NOT NULL
- `grade` - REAL

### 4. Insert Student Records
Used `executemany()` and parameterized SQL placeholders (`?`) to insert three student records.

### 5. Retrieve Records
Used `SELECT *` and `fetchall()` to retrieve and print all records.

### 6. Create a Persistent Database
Created `students.db` using a file-based SQLite connection. Used `CREATE TABLE IF NOT EXISTS` and `INSERT OR IGNORE` to avoid duplicate records.

### 7. Verify Database
Used the SQLite command-line tool to count and display stored records.

## Expected Output

```text
(1, 'Alice', 85.5)
(2, 'Bob', 78.0)
(3, 'Charlie', 92.0)
```

Database query output:

```text
3
1|Alice|85.5
2|Bob|78.0
3|Charlie|92.0
```

## Verification

- Python syntax compilation passed.
- Database contains three student records.
- SQLite integrity check returned `ok`.
- LMS assessment score: **100/100**

## Files

- `lab.py` - In-memory SQLite example.
- `lab_file.py` - Persistent SQLite database example.
- `students.db` - SQLite database file.
- `evidence/` - Lab execution and verification outputs.

## Commands to Run

```bash
python3 lab.py
python3 lab_file.py
sqlite3 students.db 'SELECT * FROM students;'
sqlite3 students.db 'PRAGMA integrity_check;'
```

## Result

Successfully completed Basic SQLite Usage and passed the Al Nafi LMS assessment with **100/100**.
