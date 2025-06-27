import requests
import json

# Replace with your actual API URL
url = "http://127.0.0.1:8080/api/products/"

# List of product JSONs you can load from a file 
"""with open("data.json", "r") as f:
    for line in f:
        product = json.loads(line)
        response = requests.post(url, json=product)
        if response.status_code == 201:
            print("Product created:")
        else:
            print("Failed to create:", response.status_code, response.text)
"""

"""product={
    'name':'vicks',
    'description':'used for many purpose',
    'domain':'healthcare',
    'price':'100'
}"""

response = requests.get(url)  # fetch you the product list
#response = requests.post(url,json=product)  

if response.status_code == 201:
    print("Product created:")
else:
    print("Failed to create:", response.status_code, response.text)