# Lab 39 - Python Style and PEP 8 Checks

## 1. Introduction

Python code should be clean, readable, and properly formatted.

PEP 8 is the official Python style guide. It provides rules for writing consistent Python code.

In this lab, I learned how to check and improve Python code using three tools:

- Flake8
- Black
- autopep8

## 2. Objectives

- Understand Python PEP 8 guidelines.
- Identify coding style mistakes.
- Check Python code using Flake8.
- Automatically format code using Black.
- Automatically format code using autopep8.
- Compare the output of both formatters.

## 3. Tools and Versions

| Tool | Version | Purpose |
|---|---|---|
| Python | 3.12.3 | Run Python programs |
| Flake8 | 7.1.1 | Find style errors |
| Black | 24.8.0 | Format Python code |
| autopep8 | 2.3.1 | Fix PEP 8 issues |

## 4. What is PEP 8?

PEP 8 stands for Python Enhancement Proposal 8.

It is a set of guidelines for writing readable and consistent Python code.

Examples of PEP 8 rules:

- Use proper spacing around operators.
- Use consistent indentation.
- Avoid unnecessary spaces.
- Write one statement per line.
- Use meaningful variable and function names.

## 5. What is Flake8?

Flake8 is a Python code checking tool.

It identifies coding style problems and some programming errors.

Command:

```bash
flake8 example.py
```

In this lab, Flake8 detected 9 style violations in the original script.

Some error codes were:

- E201 - Whitespace after opening brace.
- E202 - Whitespace before closing brace.
- E203 - Incorrect whitespace around punctuation.
- E225 - Missing whitespace around an operator.
- E231 - Missing whitespace after a colon.
- E275 - Missing whitespace after a keyword.
- E701 - Multiple statements on one line.

## 6. What is Black?

Black is an automatic Python code formatter.

It reformats code into a consistent style.

Command:

```bash
black black_version.py
```

Result:

- Corrected spacing.
- Standardized quotation marks.
- Improved if/else formatting.
- Passed Flake8 with zero errors.

## 7. What is autopep8?

autopep8 is another Python formatting tool.

It automatically fixes many PEP 8 style violations.

Command:

```bash
autopep8 --in-place --aggressive --aggressive autopep8_version.py
```

Result:

- Corrected spacing.
- Fixed multiple statements on one line.
- Improved code formatting.
- Passed Flake8 with zero errors.

## 8. Difference Between Black and autopep8

| Black | autopep8 |
|---|---|
| Applies its own consistent formatting style. | Focuses on fixing PEP 8 violations. |
| Uses double quotes in this example. | Preserves single quotes in this example. |
| Removes unnecessary parentheses around the condition. | Keeps parentheses in this example. |

Both tools successfully formatted the code.

## 9. Important Commands

```bash
python3 --version
flake8 --version
black --version
autopep8 --version

flake8 example.py
flake8 --statistics -qq example.py
flake8 --count -qq example.py

black black_version.py

autopep8 --in-place --aggressive --aggressive autopep8_version.py

python3 -m py_compile black_version.py autopep8_version.py

flake8 black_version.py autopep8_version.py
```

## 10. Final Verification

- Original code: 9 Flake8 violations detected.
- Flake8 statistics: Verified.
- Black formatting: Successful.
- autopep8 formatting: Successful.
- Python syntax check: Passed.
- Final Flake8 check: Zero errors.

## 11. What I Learned

In this lab, I learned how to write clean and readable Python code.

I understood how Flake8 detects style violations and how Black and autopep8 automatically improve code formatting.

I also learned that different formatting tools can produce slightly different results while both following PEP 8 requirements.

## 12. Conclusion

Lab 39 was completed successfully.

I practiced Python code style checking, automatic formatting, syntax verification, and comparison of formatting tools.

**LMS Result: 100/100**
