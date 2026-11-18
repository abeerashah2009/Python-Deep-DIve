# Lab 34: Simple Scripting for File Management

## Objective

Learn how to automate basic file management tasks using Python's `os` and `shutil` modules.

## Tools Used

- Python 3.12.3
- Ubuntu 24.04
- `os` module
- `shutil` module

## Concepts Learned

### 1. Import Required Modules

- `os`: Used for directory and file operations.
- `shutil`: Used to copy files and directories.

```python
import os
import shutil
```

### 2. List Files in a Directory

`os.listdir()` returns all entries inside a directory, including subdirectories.

```python
directory = os.path.expanduser('~/lab/src')
files = os.listdir(directory)
print("Files in Directory:", sorted(files))
```

### 3. Copy Files

`os.makedirs()` creates the destination directory.

`os.path.isfile()` checks whether an entry is a regular file.

`shutil.copy()` copies the file to the destination.

```python
destination = os.path.expanduser('~/lab/dst')
os.makedirs(destination, exist_ok=True)

for file in files:
    source_path = os.path.join(directory, file)
    if os.path.isfile(source_path):
        shutil.copy(source_path, destination)
```

### 4. Rename Backup Copies

`os.path.splitext()` separates the filename and extension.

An `_backup` suffix is added before the extension.

```python
base, extension = os.path.splitext(file)
new_name = f"{base}_backup{extension}"
shutil.copy(source_path, os.path.join(destination, new_name))
```

### 5. Verify File Integrity

- `sha256sum` checks file hashes.
- `diff` compares file contents.
- `cmp` checks whether two files are identical.

## Practical Tasks Completed

1. Imported `os` and `shutil`.
2. Created a source directory with five sample files.
3. Created an `archive` subdirectory.
4. Listed all directory entries.
5. Created the destination directory.
6. Copied five regular files.
7. Created five renamed backup copies.
8. Verified original and backup copies.

## Execution

Run the script:

```bash
python3 filemgr.py
```

## Verification Results

- Python syntax check: PASSED
- Source files: 5
- Destination files: 10
- Original file copies: Identical
- Backup copies: Identical
- SHA-256 verification: PASSED
- `diff` verification: PASSED
- Archive directory correctly excluded from copying.

See `evidence/verification.txt` for verification output.

## Advantages of Script-Based File Management

- **Automation:** Reduces repetitive manual work.
- **Scalability:** Can process many files.
- **Accuracy:** Reduces human errors.
- **Customization:** Allows additional conditions and logging.

## Conclusion

Successfully completed a Python file management script using `os` and `shutil`. Practised listing, copying, renaming, and verifying files through automation.

**LMS Result: 95 / 100 — Passed**
