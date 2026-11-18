# Lab 24: Basic Regular Expressions

## Overview

This lab introduces Regular Expressions (Regex) in Python using the built-in `re` module.

Regular expressions are patterns used to search, match, extract, and replace text.

## Objectives

- Understand basic regular expression concepts.
- Learn how to use Python's `re` module.
- Compile regex patterns.
- Find and replace patterns in strings.
- Use special characters and capturing groups.
- Understand named groups and `finditer()`.

## Environment

| Component | Details |
|---|---|
| Operating System | Ubuntu 24.04 LTS |
| Python | 3.12.3 |
| Module | re |
| Script | regex_lab.py |
| External packages | Not required |

## 1. Introduction to Regular Expressions

A regular expression is a sequence of characters that defines a search pattern.

Python provides the built-in `re` module for regular expression operations.

Import the module:

```python
import re
```

No additional package installation is required.

## 2. Important Regex Special Characters

| Pattern | Meaning | Example |
|---|---|---|
| `\d` | Matches a digit | `7` |
| `\d+` | Matches one or more digits | `2021` |
| `\w` | Matches a word character | `A`, `b`, `5` |
| `\s` | Matches whitespace | Space |
| `.` | Matches any character except newline by default | `a` |
| `^` | Matches the beginning of a string | `^Hello` |
| `$` | Matches the end of a string | `end$` |
| `*` | Matches zero or more repetitions | `a*` |
| `+` | Matches one or more repetitions | `a+` |
| `?` | Matches zero or one repetition | `colou?r` |
| `{n}` | Matches exactly n repetitions | `\d{4}` |
| `()` | Creates a capturing group | `(\d+)` |

## 3. Raw Strings

Regex patterns should normally use raw strings such as:

```python
r"\d+"
```

The `r` prefix tells Python to treat backslashes as literal characters rather than interpreting them as Python string escapes.

## 4. Task 1: Importing the re Module

The `re` module is part of Python's standard library.

```python
import re
```

Verification:

```bash
python3 -c 'import re; print("import OK")'
```

Expected output:

```text
import OK
```

## 5. Task 2: Compile a Regular Expression Pattern

The `re.compile()` function creates a reusable regex pattern.

```python
pattern = re.compile(r"\d+")
```

Explanation:

- `re.compile()` compiles the pattern.
- `\d` matches a digit.
- `+` matches one or more consecutive digits.
- The raw string prefix `r` handles backslashes correctly.

## 6. Task 3: Find All Matches

The `findall()` method returns all matches as a list.

```python
test_string = "The rainfall 2021 was greater than 2019 and 2020 combined."

matches = pattern.findall(test_string)

print("Matches found:", matches)
```

Expected output:

```text
Matches found: ['2021', '2019', '2020']
```

An assertion verifies that the result is correct:

```python
assert matches == ['2021', '2019', '2020']
```

## 7. Task 4: Replace Matches

The `sub()` method replaces all matches with another string.

```python
replaced_string = pattern.sub("XXXX", test_string)

print("Replaced String:", replaced_string)
```

Expected output:

```text
Replaced String: The rainfall XXXX was greater than XXXX and XXXX combined.
```

Verification:

```python
assert replaced_string == "The rainfall XXXX was greater than XXXX and XXXX combined."
```

## 8. Task 5: Groups and Special Characters

### Capturing Groups

Parentheses `()` create capturing groups.

Example:

```python
date_pattern = re.compile(r"(\d{4})-(\d{2})-(\d{2})")

date_string = "Date of birth: 1990-08-15 and starting date 2020-01-01."

date_matches = date_pattern.findall(date_string)
```

Expected output:

```text
Date Matches: [('1990', '08', '15'), ('2020', '01', '01')]
```

Each tuple contains three captured values:

- Year
- Month
- Day

### Named Groups

Named groups make regex patterns easier to understand.

Syntax:

```python
(?P<name>pattern)
```

Example:

```python
named_date_pattern = re.compile(
    r"(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})"
)

for match in named_date_pattern.finditer(date_string):
    print(
        "Year:", match.group("year"),
        "Month:", match.group("month"),
        "Day:", match.group("day")
    )
```

Expected output:

```text
Year: 1990 Month: 08 Day: 15
Year: 2020 Month: 01 Day: 01
```

`finditer()` returns match objects, and `group()` retrieves a named captured value.

## 9. Complete Python Program

File: `regex_lab.py`

```python
import re

# Task 2: Compile a regular expression pattern
pattern = re.compile(r"\d+")

# Task 3: Find all digit matches
test_string = "The rainfall 2021 was greater than 2019 and 2020 combined."
matches = pattern.findall(test_string)
print("Matches found:", matches)
assert matches == ['2021', '2019', '2020']

# Task 4: Replace all digit matches
replaced_string = pattern.sub("XXXX", test_string)
print("Replaced String:", replaced_string)
assert replaced_string == "The rainfall XXXX was greater than XXXX and XXXX combined."

# Task 5: Capture date groups
date_pattern = re.compile(r"(\d{4})-(\d{2})-(\d{2})")
date_string = "Date of birth: 1990-08-15 and starting date 2020-01-01."
date_matches = date_pattern.findall(date_string)
print("Date Matches:", date_matches)
assert date_matches == [('1990', '08', '15'), ('2020', '01', '01')]

# Task 5: Use named groups
named_date_pattern = re.compile(r"(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})")
for match in named_date_pattern.finditer(date_string):
    print("Year:", match.group("year"), "Month:", match.group("month"), "Day:", match.group("day"))
```

## 10. Run and Verify the Program

Run:

```bash
python3 regex_lab.py
```

Expected output:

```text
Matches found: ['2021', '2019', '2020']
Replaced String: The rainfall XXXX was greater than XXXX and XXXX combined.
Date Matches: [('1990', '08', '15'), ('2020', '01', '01')]
Year: 1990 Month: 08 Day: 15
Year: 2020 Month: 01 Day: 01
```

All assertions passed when the program completed without an error.

## 11. Important Validation Limitation

The date pattern checks the structure of a date, not whether it is a valid calendar date.

For example, it can match `9999-99-99`.

For real date validation, use Python's `datetime.date` and check valid month and day ranges.

## 12. Evidence Files

The `evidence/` directory contains:

1. `python-version.txt` — Python version.
2. `import-check.txt` — Successful re module import.
3. `compile-pattern.txt` — Compiled regex pattern.
4. `findall-output.txt` — Digit matching output.
5. `replace-output.txt` — Replacement output.
6. `date-groups-output.txt` — Captured date groups.
7. `named-groups-output.txt` — Named group output.
8. `full-run-output.txt` — Complete program output.
9. `syntax-check.txt` — Python syntax verification.
10. `code-structure.txt` — Important code statements.

## 13. Interview Questions and Answers

**Q1. What is a regular expression?**

A regular expression is a pattern used to search, match, and replace text.

**Q2. Which module handles regex in Python?**

Python uses the built-in `re` module.

**Q3. What does `\d` match?**

It matches a digit from 0 to 9.

**Q4. What does `+` mean in regex?**

It means one or more repetitions of the preceding pattern.

**Q5. What is `re.compile()`?**

It compiles a regex pattern so it can be reused.

**Q6. What does `findall()` return?**

It returns a list containing all matches.

**Q7. What is the purpose of `sub()`?**

It replaces matching text with a replacement string.

**Q8. What are capturing groups?**

Parentheses `()` capture parts of a regex match.

**Q9. What are named groups?**

Named groups assign readable names to captured parts using `(?P<name>...)`.

**Q10. What is the difference between `findall()` and `finditer()`?**

`findall()` returns matched values in a list, while `finditer()` returns an iterator of match objects.

## 14. Conclusion

In this lab, I practiced regular expressions using Python's built-in `re` module.

I learned how to compile patterns, find digit matches, replace text, capture date groups, and use named groups with `finditer()`.

These skills are useful for text processing, data extraction, input checking, and automation tasks.

**Lab 24: Basic Regular Expressions — Completed and Verified.**
