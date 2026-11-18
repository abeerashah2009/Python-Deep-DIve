# Lab 25: Intro to Unit Testing with unittest

## 1. Introduction

Unit testing is a software testing method used to check whether
individual parts of a program work correctly.

Python provides a built-in module called `unittest` for writing
and running unit tests.

## 2. Objectives

- Understand the basics of unit testing.
- Learn about Python's unittest module.
- Create a Python module.
- Write test cases using unittest.
- Use assertions to check expected results.
- Identify and fix a failing test.

## 3. Project Structure

```text
Lab-25-Intro-to-Unit-Testing-with-unittest/
├── README.md
├── mymath.py
├── test_example.py
└── evidence/
```

## 4. Create a Python Module

File: `mymath.py`

```python
def add(a, b):
    return a + b
```

**Explanation:**

- `def` defines a function.
- `add` is the function name.
- `a` and `b` are the input arguments.
- `return` sends back the sum.

Example:

```python
add(2, 3)
```

Output:

```text
5
```

## 5. Create Unit Tests

File: `test_example.py`

```python
import unittest
from mymath import add


class TestMath(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)

    def test_add_wrong(self):
        self.assertEqual(add(2, 2), 4)


if __name__ == "__main__":
    unittest.main()
```

**Explanation:**

- `import unittest` imports the testing module.
- `from mymath import add` imports the function.
- `unittest.TestCase` provides the test case class.
- `test_add()` checks the addition function.
- `assertEqual()` compares the actual and expected values.
- `unittest.main()` runs tests when the file is executed directly.

## 6. Run Unit Tests

Command:

```bash
cd ~/lab/unit
python3 -m unittest discover -v
```

Expected output:

```text
test_add ... ok

Ran 1 test

OK
```

**Meaning:**

- `ok` means the test passed.
- `Ran 1 test` means one test was executed.
- `OK` means all executed tests passed.

## 7. Understand a Failed Test

We intentionally used an incorrect expected value:

```python
self.assertEqual(add(2, 2), 5)
```

Actual result:

```text
4
```

Expected result:

```text
5
```

The test reported:

```text
AssertionError: 4 != 5
```

Exit code:

```text
1
```

**Important:** A failed test helps identify an incorrect result or
an incorrect expectation.

## 8. Fix the Failed Test

Correct assertion:

```python
self.assertEqual(add(2, 2), 4)
```

Command used:

```bash
sed -i 's/add(2, 2), 5/add(2, 2), 4/' test_example.py
```

Run the tests again:

```bash
python3 -m unittest discover -v
```

Final result:

```text
test_add ... ok
test_add_wrong ... ok

Ran 2 tests

OK
```

Exit code:

```text
0
```

## 9. Python Syntax Verification

Command:

```bash
python3 -m py_compile mymath.py test_example.py
```

No output means the Python files passed the syntax check.

## 10. Important Commands

| Command | Purpose |
|---|---|
| `python3 --version` | Check Python version |
| `python3 -m unittest discover -v` | Discover and run tests |
| `python3 -m py_compile mymath.py test_example.py` | Check Python syntax |
| `echo $?` | Check the previous command's exit code |

## 11. Key Concepts Learned

- Unit testing checks individual program components.
- `unittest` is included in Python.
- Test methods normally begin with `test_`.
- `assertEqual()` compares two values.
- A passing test displays `ok`.
- A failing test displays `FAIL`.
- Exit code `0` indicates success.
- Exit code `1` indicates test failure.

## 12. Lab Result

**LMS Score: 100 / 100**

**Status: PASSED**

Both final unit tests passed successfully.

## 13. Conclusion

In this lab, I learned how to create and test a Python function
using the unittest framework. I also demonstrated a failing test,
corrected the expected value, and verified that both tests passed.

This lab helped me understand how unit testing identifies errors
and improves the reliability of Python programs.
