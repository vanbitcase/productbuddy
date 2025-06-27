import requests

product_id = 1  # Replace with the actual product ID you want to delete
url = f"http://127.0.0.1:8080/api/products/{product_id}/"

response = requests.delete(url)

if response.status_code == 204:
    print("Product deleted successfully.")
elif response.status_code == 404:
    print("Product not found.")
else:
    print("Error:", response.status_code, response.text)