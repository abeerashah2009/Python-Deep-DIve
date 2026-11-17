import requests

response = requests.get("http://localhost:8000/data.json", timeout=10)
response.raise_for_status()
print(response.status_code)
print(response.headers["content-type"])
