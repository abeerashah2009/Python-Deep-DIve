# Lab 23: Using Requests for HTTP Calls

## 1. Overview

This lab demonstrates how to use the Python `requests` library to communicate with an HTTP server.

The practical exercises use a local JSON server to demonstrate HTTP GET requests, response status codes, content types, and JSON parsing.

## 2. Objectives

- Install and import the Python Requests library.
- Create and use a Python virtual environment.
- Send HTTP GET requests.
- Inspect HTTP response status codes.
- Check HTTP response headers.
- Parse JSON responses into Python dictionaries.
- Extract information from API responses.
- Understand common HTTP status codes.

## 3. Environment

| Component | Version / Details |
|---|---|
| Operating System | Ubuntu 24.04 LTS |
| Python | 3.12.3 |
| Requests | 2.32.3 |
| HTTP Server | Python HTTP Server |
| Server Port | 8000 |

## 4. Install Requests

Ubuntu 24.04 protects its system Python environment. A virtual environment was created to install Requests safely.

```bash
sudo apt update
sudo apt install -y python3 python3-venv curl

mkdir -p ~/requests-lab
cd ~/requests-lab

python3 -m venv venv
source venv/bin/activate

pip install requests==2.32.3
```

Verify the installed version:

```bash
python3 -c "import requests; print(requests.__version__)"
```

Expected output:

```text
2.32.3
```

Test the library import:

```bash
python3 -c "import requests; print(requests.get)"
```

The output confirms that the GET function is available.

## 5. Important Concepts

### HTTP Requests

HTTP (Hypertext Transfer Protocol) is used for communication between clients and servers.

### GET Request

A GET request retrieves information from a server.

```python
response = requests.get(url, timeout=10)
```

### Response Status Codes

| Status Code | Meaning |
|---|---|
| 200 | OK — request successful |
| 404 | Not Found — requested resource does not exist |
| 500 | Internal Server Error — server encountered an error |

### Response Headers

HTTP headers provide additional information about a response.

The `Content-Type` header identifies the format of the returned data.

### JSON

JSON (JavaScript Object Notation) is a common format for exchanging data between applications.

The Requests library provides `response.json()` to convert JSON response data into Python objects.

## 6. Create a Local JSON Server

The following JSON data was saved in `data.json`:

```json
{
  "status": "ok",
  "name": "demo-api",
  "version": 1,
  "repos": ["alpha", "beta"]
}
```

Start the local server:

```bash
cd ~/requests-lab

python3 -m http.server 8000 >server.log 2>&1 &

echo $! > server.pid
```

Verify the server:

```bash
curl -fs --retry 20 --retry-delay 2 --retry-all-errors \
-o /dev/null -w '%{http_code}\n' localhost:8000/data.json
```

Expected result:

```text
200
```

## 7. Task 1: Basic HTTP GET Request

File: `get.py`

```python
import requests

response = requests.get("http://localhost:8000/data.json", timeout=10)
response.raise_for_status()

print(response.status_code)
print(response.headers["content-type"])
```

Expected output:

```text
200
application/json
```

Explanation:

- `import requests` imports the library.
- `requests.get()` sends an HTTP GET request.
- `timeout=10` limits the waiting time.
- `raise_for_status()` raises an exception for unsuccessful HTTP responses.
- `response.status_code` displays the HTTP status code.
- `response.headers` provides response header information.

### Test HTTP 404

Command:

```bash
curl -s -o /dev/null -w '%{http_code}\n' localhost:8000/missing.json
```

Output:

```text
404
```

This confirms that the server returns a Not Found response for a missing file.

## 8. Task 2: Parse JSON Response

File: `parse.py`

```python
import requests

response = requests.get("http://localhost:8000/data.json", timeout=10)
response.raise_for_status()

response_data = response.json()

print(type(response_data))
print(response_data["status"], response_data["name"])
```

Expected output:

```text
<class 'dict'>
ok demo-api
```

Explanation:

- `response.json()` converts the JSON response into a Python dictionary.
- `type(response_data)` checks the returned data type.
- Dictionary keys are used to access individual values.

## 9. Task 3: Read API Data

File: `repos.py`

```python
import requests

data = requests.get("http://localhost:8000/data.json", timeout=10).json()

print("status:", data["status"])
print("repos:", ", ".join(data["repos"]))
```

Expected output:

```text
status: ok
repos: alpha, beta
```

Compare the Python result with the original JSON:

```bash
curl -s localhost:8000/data.json
```

Output:

```json
{"status": "ok", "name": "demo-api", "version": 1, "repos": ["alpha", "beta"]}
```

The Python program successfully extracted the status and repository names from the API response.

## 10. Clean Up the Local Server

Stop the background HTTP server:

```bash
kill $(cat ~/requests-lab/server.pid)
```

Deactivate the virtual environment:

```bash
deactivate
```

Verify that the server has stopped:

```bash
ss -ltnp | grep ':8000' || echo "Port 8000 is closed"

curl --noproxy '*' -s -o /dev/null -w '%{http_code}\n' \
http://localhost:8000/data.json
```

Verified output:

```text
Port 8000 is closed
000
```

## 11. Verification Results

| Verification | Result |
|---|---|
| Python 3.12.3 available | Passed |
| Requests 2.32.3 installed | Passed |
| Requests import | Passed |
| Local JSON server | Passed |
| HTTP GET request | Passed |
| HTTP 200 response | Passed |
| Content-Type header | Passed |
| HTTP 404 response | Passed |
| JSON dictionary parsing | Passed |
| API status extraction | Passed |
| Repository list extraction | Passed |
| curl JSON comparison | Passed |
| Server cleanup | Passed |
| Python syntax compilation | Passed |

## 12. Evidence Files

The `evidence/` directory contains:

- `python-version.txt`
- `requests-version.txt`
- `compile-check.txt`
- `code-structure.txt`
- `get-request-output.txt`
- `http-404-output.txt`
- `json-parsing-output.txt`
- `api-data-output.txt`
- `curl-json-output.txt`
- `server-cleanup-output.txt`

## 13. Interview Questions and Answers

**Q1. What is the Requests library?**

Requests is a Python library used to send HTTP requests and communicate with web servers and APIs.

**Q2. What is an HTTP GET request?**

A GET request retrieves information from a server.

**Q3. What does HTTP status code 200 mean?**

It means the request was successful.

**Q4. What does HTTP status code 404 mean?**

It means the requested resource was not found.

**Q5. What is the purpose of `requests.get()`?**

It sends an HTTP GET request to a specified URL.

**Q6. What does `response.raise_for_status()` do?**

It raises an HTTP error for unsuccessful 4xx or 5xx responses.

**Q7. What does `response.json()` do?**

It parses a JSON response and converts it into Python data structures.

**Q8. What is a Python dictionary?**

A dictionary stores data as key-value pairs.

**Q9. Why is a timeout important?**

A timeout prevents a request from waiting indefinitely for a response.

**Q10. What is an API?**

An API (Application Programming Interface) allows different software applications to communicate and exchange data.

## 14. Conclusion

In this lab, I learned how to install and import the Requests library, send HTTP GET requests, inspect response status codes and headers, and parse JSON data.

I also created a local HTTP server, extracted API information, compared the results with curl, and verified server cleanup.

These skills provide a foundation for working with REST APIs and Python-based automation.
