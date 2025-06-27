import requests


url = "http://127.0.0.1:8080/api/recommend/"
params = {"query": "AC"}  # You can write the same product name and the related names to fetch related product.
response = requests.get(url, params=params)

if response.status_code == 200:
    data = response.json()
    print("Recommendations:", data.get("recommendations", []))
    if "message" in data:
        print("Message:", data["message"])
else:
    print("Error:", response.status_code, response.text)