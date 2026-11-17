import requests

response = requests.get("http://localhost:8000/data.json", timeout=10)
response.raise_for_status()
response_data = response.json()
print(type(response_data))
print(response_data["status"], response_data["name"])
