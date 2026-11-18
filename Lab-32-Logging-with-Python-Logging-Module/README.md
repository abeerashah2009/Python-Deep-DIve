# Lab 32 - Logging with Python's Logging Module

## 1. Objective

Learn how to use Python's built-in logging module to record application activities, track errors, and troubleshoot problems.

## 2. Tools and Environment

- Operating System: Ubuntu 24.04
- Python Version: 3.12.3
- Module: logging
- Editor: Nano

## 3. Introduction to Logging

Logging is used to record information about what happens while a program is running.

It helps developers:
- Monitor application activity.
- Identify errors and problems.
- Debug applications.
- Track application behavior.
- Maintain software more easily.

Python provides a built-in module called `logging`. No additional installation is required.

## 4. Import the Logging Module

```python
import logging
```

The logging module is part of Python's standard library.

## 5. Logging Levels

Python provides five main logging levels.

| Level | Purpose |
|---|---|
| DEBUG | Detailed information for troubleshooting. |
| INFO | Confirms that something is working correctly. |
| WARNING | Indicates a possible problem. |
| ERROR | Reports a serious problem. |
| CRITICAL | Reports a very serious problem. |

## 6. Configure Logging

The `basicConfig()` function configures the logging system.

```python
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
)
```

### Explanation

- `level=logging.DEBUG`: Enables all five logging levels.
- `%(asctime)s`: Displays the timestamp.
- `%(levelname)s`: Displays the logging level.
- `%(message)s`: Displays the log message.

**Important Note:** Configure the logging level and format in one `basicConfig()` call because subsequent calls normally do not change an already configured logging system.

## 7. Generate Log Messages

```python
logging.debug('This is a debug message.')
logging.info('This is an info message.')
logging.warning('This is a warning message.')
logging.error('This is an error message.')
logging.critical('This is a critical message.')
```

Example output:

```text
DEBUG - This is a debug message.
INFO - This is an info message.
WARNING - This is a warning message.
ERROR - This is an error message.
CRITICAL - This is a critical message.
```

## 8. Change the Logging Threshold

The logging threshold determines which messages are displayed.

Example:

```python
logging.basicConfig(level=logging.WARNING)
```

When the threshold is WARNING, only these messages appear:

- WARNING
- ERROR
- CRITICAL

DEBUG and INFO messages are ignored.

## 9. Save Logs into a File

Python can save log records into a file instead of displaying them in the terminal.

```python
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='app.log',
    filemode='w',
)
```

### Important Parameters

- `filename`: Specifies the log file name.
- `filemode='w'`: Creates or overwrites the log file.
- `level`: Sets the minimum logging level.
- `format`: Defines the log message format.

## 10. Practical Application: Division Error Handling

```python
def divide_numbers(a, b):
    try:
        result = a / b
        logging.info('Division successful.')
        return result
    except ZeroDivisionError:
        logging.exception('Division by zero error.')
        return None

result = divide_numbers(10, 0)
```

### Explanation

- `try`: Executes the division operation.
- `except`: Handles division by zero.
- `ZeroDivisionError`: Python exception raised when dividing by zero.
- `logging.exception()`: Records the error and full traceback.
- `return None`: Returns None when division fails.

**Important Note:** `logging.exception()` should be used inside an exception handler. It logs at ERROR level and includes traceback information.

## 11. Verify ERROR Records

Command:

```bash
grep -c ERROR app.log
```

Expected output:

```text
2
```

The two ERROR records are:
1. The manually generated error message.
2. The division-by-zero exception.

## 12. Important Commands

| Command | Purpose |
|---|---|
| `python3 --version` | Check Python version. |
| `python3 log_demo.py` | Run the Python application. |
| `cat app.log` | Display saved log records. |
| `grep -c ERROR app.log` | Count ERROR records. |
| `python3 -m py_compile log_demo.py` | Check Python syntax. |

## 13. Files Included

- `log_demo.py` - Python logging application.
- `evidence/01-module-import.txt` - Module import verification.
- `evidence/02-debug-level-output.txt` - Logging level output.
- `evidence/04-verification.txt` - Syntax and ERROR count verification.
- `evidence/app.log` - Application log records and exception traceback.

## 14. Verification Results

- Python logging module imported successfully.
- All five logging levels tested.
- DEBUG threshold tested.
- WARNING threshold tested.
- Log formatting verified.
- Log records successfully saved to `app.log`.
- Division-by-zero exception handled.
- Full traceback recorded.
- ERROR record count verified as 2.
- Python syntax compilation successful.

## 15. LMS Assessment

**Lab Score: 100/100**

Status: Passed

## 16. Conclusion

Successfully completed Lab 32 using Python's built-in logging module.

Learned how to configure logging levels, format log messages, save records into files, and handle exceptions with traceback information.

Logging is an important skill in Python development, application monitoring, debugging, and DevOps operations.
