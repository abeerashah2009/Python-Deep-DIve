# Lab 31 - CLI Applications with argparse

## Objective
Learn how to build command-line applications in Python using the `argparse` module.

## Tools and Environment
- Ubuntu 24.04
- Python 3.12.3
- Python argparse module

## Tasks Completed

### 1. Import argparse
Imported Python's built-in `argparse` module.

### 2. Create an Argument Parser
Created an `ArgumentParser` with the description:
`A simple greeting application.`

### 3. Define Command-Line Arguments
- `--name`: Accepts a person's name as text.
- `--count`: Accepts an integer.
- Default count: `1`.
- Allowed choices: `1`, `2`, or `3`.

### 4. Parse Arguments
Used `parse_args()` to read command-line arguments.

### 5. Generate Greetings
Printed a greeting using the supplied name. If no name is provided, the application uses `Stranger`.

### 6. Handle Invalid Arguments
Tested an unknown argument and an invalid count. Both produced an error and exit code `2`.

### 7. Executable Script
Used `chmod +x greet.py` to make the script executable.

### 8. Automatic Help Generation
Used `--help` to display the application's usage instructions and argument descriptions.

## Example Output

```text
Hello, Alice!
Hello, Stranger!
Hello, Alice!
Hello, Alice!
```

## Invalid Input Verification

- Unknown argument: `--bad`
- Invalid count: `--count 5`
- Expected exit code: `2`

## Help Command

```bash
python3 greet.py --help
```

## Verification

- Python syntax compilation passed.
- Executable permission verified.
- Default name and count tested.
- Valid and invalid arguments tested.
- Automatic help text verified.
- LMS assessment score: **100/100**

## Files

- `greet.py` - Python command-line greeting application.
- `evidence/` - Lab execution and verification outputs.

## Run the Application

```bash
python3 greet.py --name Alice
python3 greet.py
python3 greet.py --name Alice --count 2
python3 greet.py --help
```

## Result

Successfully completed CLI Applications with argparse and passed the Al Nafi LMS assessment with **100/100**.
