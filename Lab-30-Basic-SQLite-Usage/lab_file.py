import sqlite3

connection = sqlite3.connect('students.db')
cursor = connection.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS students (id INTEGER PRIMARY KEY, name TEXT NOT NULL, grade REAL)")
cursor.executemany("INSERT OR IGNORE INTO students VALUES (?, ?, ?)", [
    (1, 'Alice', 85.5),
    (2, 'Bob', 78.0),
    (3, 'Charlie', 92.0)
])
connection.commit()
connection.close()
