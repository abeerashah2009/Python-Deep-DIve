import requests

data = requests.get("http://localhost:8000/data.json", timeout=10).json()
print("status:", data["status"])
print("repos:", ", ".join(data["repos"]))
