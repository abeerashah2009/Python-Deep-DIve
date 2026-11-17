# Lab 16: Python Virtual Environments (venv)

## 1. Introduction

A Python Virtual Environment is an isolated workspace where we can install Python packages separately for each project.

It helps us manage different package versions without affecting the system Python or other projects.

**Example:**
- Project A uses requests 2.25.1.
- Project B uses requests 2.32.3.

Both projects can work independently using separate virtual environments.

## 2. Objectives

- Understand Python virtual environments.
- Learn how to create a virtual environment.
- Activate and deactivate a virtual environment.
- Install Python packages inside a virtual environment.
- Manage dependencies using requirements.txt.
- Understand package isolation.

## 3. System Requirements

| Component | Version / Details |
|---|---|
| Operating System | Ubuntu 24.04 LTS |
| Python | 3.12.3 |
| Virtual Environment | venv |
| Package | requests |
| Package Version | 2.32.3 |

## 4. What is venv?

`venv` is a built-in Python module used to create virtual environments.

It creates a separate directory containing:
- Python executable
- pip package installer
- Installed libraries
- Environment configuration

**Command:**

```bash
python3 -m venv myenv
```

This creates a virtual environment named `myenv`.

## 5. Install Virtual Environment Support

On Ubuntu, install the venv support package:

```bash
sudo apt update
sudo apt install -y python3.12-venv
```

**Explanation:**
- `apt update` updates package information.
- `apt install` installs software.
- `python3.12-venv` provides virtual environment support for Python 3.12.

## 6. Create a Project Directory

```bash
mkdir -p ~/my_project
cd ~/my_project
```

**Explanation:**
- `mkdir` creates a directory.
- `-p` creates parent directories if needed.
- `cd` changes the current directory.

## 7. Create a Virtual Environment

```bash
python3 -m venv myenv
```

Check its contents:

```bash
ls myenv
```

**Output:**

```text
bin  include  lib  lib64  pyvenv.cfg
```

**Directory explanation:**

- `bin`: Contains Python and pip executables.
- `include`: Contains development header files.
- `lib`: Stores installed Python packages.
- `lib64`: Library directory or symbolic link.
- `pyvenv.cfg`: Stores virtual environment configuration.

## 8. Activate the Virtual Environment

```bash
source myenv/bin/activate
```

Check Python location:

```bash
which python
```

**Output:**

```text
/home/ubuntu/my_project/myenv/bin/python
```

When activated, `(myenv)` appears in the terminal prompt.

This means commands use the virtual environment's Python.

## 9. Install a Python Package

Install the required requests version:

```bash
pip install requests==2.32.3
```

**Explanation:**
- `pip` is Python's package installer.
- `install` installs a package.
- `requests` is a Python HTTP library.
- `==2.32.3` specifies the exact version.

## 10. Verify Installed Packages

Display installed packages:

```bash
pip list
```

Check the requests version:

```bash
python -c 'import requests;print(requests.__version__)'
```

**Expected result:**

```text
2.32.3
```

This confirms that requests is installed and working inside the virtual environment.

## 11. What is requirements.txt?

`requirements.txt` is a file that records project dependencies and their versions.

Create it using:

```bash
pip freeze > requirements.txt
```

Display its contents:

```bash
cat requirements.txt
```

**Our recorded dependencies:**

```text
certifi==2026.10.23
charset-normalizer==3.5.2
idna==3.20
requests==2.32.3
urllib3==2.8.0
```

**Important:** Pinning package versions helps reproduce the same project environment.

## 12. Deactivate the Virtual Environment

```bash
deactivate
```

This returns the terminal to the normal system environment.

The `(myenv)` prefix disappears.

## 13. Create a Second Virtual Environment

Create another environment:

```bash
python3 -m venv myenv2
```

Install dependencies from the requirements file:

```bash
myenv2/bin/pip install -r requirements.txt
```

Here:
- `-r` reads the requirements file.
- `pip install` installs all listed dependencies.
- `myenv2` keeps these packages separate from the first environment.

## 14. Verify the Second Environment

Check requests version:

```bash
myenv2/bin/python -c 'import requests;print(requests.__version__)'
```

Check Python executable:

```bash
myenv2/bin/python -c 'import sys;print(sys.executable)'
```

**Verified results:**

```text
2.32.3
/home/ubuntu/my_project/myenv2/bin/python
```

## 15. Understanding Dependency Isolation

Our practical results:

| Python Environment | Requests Version |
|---|---|
| System Python | 2.31.0 |
| myenv | 2.32.3 |
| myenv2 | 2.32.3 |

This confirms that each environment can maintain its own package version.

### What is PEP 668?

PEP 668 defines how Python distributions can mark their system Python environment as externally managed.

This helps prevent pip from making changes that could damage operating-system-managed Python packages.

**Lab observation:** The `pip3` command was not available globally. System Python already contained requests 2.31.0 from Ubuntu's package directory. We recorded the actual result instead of assuming a PEP 668 error.

## 16. Important Commands Revision

| Command | Purpose |
|---|---|
| `python3 --version` | Check Python version |
| `python3 -m venv myenv` | Create environment |
| `source myenv/bin/activate` | Activate environment |
| `which python` | Find active Python |
| `pip install requests==2.32.3` | Install package |
| `pip list` | List installed packages |
| `pip freeze` | Display dependency versions |
| `pip freeze > requirements.txt` | Save dependencies |
| `deactivate` | Exit environment |
| `pip install -r requirements.txt` | Install saved dependencies |

## 17. Real-World Use Cases

Virtual environments are useful in:

1. **Web Development:** Different applications may require different package versions.
2. **Data Science:** Projects can maintain separate libraries.
3. **Machine Learning:** Different models may require different dependencies.
4. **DevOps:** Python automation scripts can use controlled dependencies.
5. **Team Projects:** Developers can install consistent package versions using requirements.txt.

## 18. Common Interview Questions

**Q1. What is a virtual environment?**

A virtual environment is an isolated Python workspace that maintains separate packages for a project.

**Q2. Why do we use venv?**

We use venv to avoid dependency conflicts between projects.

**Q3. How do you create a virtual environment?**

```bash
python3 -m venv myenv
```

**Q4. How do you activate it?**

```bash
source myenv/bin/activate
```

**Q5. How do you deactivate it?**

```bash
deactivate
```

**Q6. What is pip?**

pip is a package installer used to install and manage Python packages.

**Q7. What is requirements.txt?**

It is a file containing project dependencies and their versions.

**Q8. What does pip freeze do?**

It displays installed packages with their exact versions.

**Q9. What is dependency isolation?**

Dependency isolation means each project can maintain its own packages without affecting other projects.

**Q10. What is PEP 668?**

PEP 668 provides a mechanism for marking system Python environments as externally managed.

## 19. Lab Evidence

The following evidence files were created:

- `evidence/verification.txt`
- `evidence/requirements-output.txt`
- `evidence/environments.txt`

The dependency file is:

- `requirements.txt`

## 20. Conclusion

In this lab, I successfully created two Python virtual environments on Ubuntu 24.04.

I installed requests 2.32.3, verified the package, saved dependencies in requirements.txt, and recreated the environment using the saved dependencies.

I also compared system Python with both virtual environments and confirmed that their package versions remained separate.

**Lab 16 practical work completed successfully.**
