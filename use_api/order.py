import requests

url = "http://127.0.0.1:8080/api/orders/"
data = {
    "product_ids": [450,621,780]  #place any product id by viewing the product.csv
}

response = requests.post(url, json=data)
#response = requests.get(url) # order list

if response.status_code == 201:
    print("Order placed successfully:", response.json())
else:
    print("Error:", response.status_code, response.text)