# ProductBuddy

ProductBuddy is a Django-based REST API for managing products and orders, with a built-in product recommendation system using machine learning (TF-IDF and cosine similarity).

## Features

- CRUD operations for Products
- CRUD operations for Orders
- Product recommendation endpoint based on product name similarity,orders
- MySQL database support (via Docker)
- Ready-to-use API with example Python scripts for CRUD operations

---

## Getting Started

### Prerequisites

- Docker & Docker Compose
- Python 3.12+ 
- MySQL client for direct DB access

### Setup with Docker

1. Clone the repository:
   ```bash
   git clone <your-repo-url>
   cd project/productbuddy
   ```

2. Build and start the services:
   ```bash
   docker-compose up --build
   ```
   - The API will be available at `http://127.0.0.1:8080/`
   - MySQL will be available at port `3307` host → `3306` container

3. The database will be initialized with `data.sql` if present.

---

## API Endpoints

All endpoints are prefixed with `/api/`.

### Product Endpoints

- `GET /api/products/`  
  List all products.

- `POST /api/products/`  
  Create a new product.  
  **Body:**
  ```json
  {
    "name": "Product Name",
    "description": "Product description",
    "price": 100.0,
    "domain": "category"
  }
  ```

- `GET /api/products/<id>/`  
  Retrieve a product by ID.

- `PUT /api/products/<id>/`  
  Update a product.

- `DELETE /api/products/<id>/`  
  Delete a product.

#### Example: List Products (Python)
```python
import requests
url = "http://127.0.0.1:8080/api/products/"
response = requests.get(url)
print(response.json())
```

---

### Order Endpoints

- `GET /api/orders/`  
  List all orders.

- `POST /api/orders/`  
  Create a new order.  
  **Body:**
  ```json
  {
    "product_ids": [1, 2, 3]
  }
  ```

- `GET /api/orders/<id>/`  
  Retrieve an order by ID.

- `PUT /api/orders/<id>/`  
  Update an order.

- `DELETE /api/orders/<id>/`  
  Delete an order.

#### Example: Place an Order
```python
import requests
url = "http://127.0.0.1:8080/api/orders/"
data = {"product_ids": [1, 2, 3]}
response = requests.post(url, json=data)
print(response.json())
```
#### Example: To delete an product 
```python
import requests

product_id = 1 
url = f"http://127.0.0.1:8080/api/products/{product_id}/"

response = requests.delete(url)

if response.status_code == 204:
    print("Product deleted successfully.")
else:
    print("Error:", response.status_code, response.text)
```

---

### Product Recommendation Endpoint

- `GET /api/recommend/?query=<product_name>`  
  Get product recommendations based on a product name or keyword.

  **Response:**
  ```json
  {
    "recommendations": {"559":"Lloyd 1.5 Ton 3 Star Inverter Split Ac","429":"Havells-Lloyd 1.5 Ton 3 Star Inverter Split AC",
  "9505":"Lloyd 1.5 Ton 3 Star Inverter Split Ac","62":"Lloyd 2.0 Ton 3 Star Inverter Split Ac",
  "5":"Lloyd 1.0 Ton 3 Star Inverter Split Ac","6":"Lloyd 1.5 Ton 5 Star Inverter Split Ac"}
  }
  ```

#### Example: Get Recommendations 
```python
import requests
url = "http://127.0.0.1:8080/api/recommend/"
params = {"query": "AC"}
response = requests.get(url, params=params)
print(response.json())
```

---

## Database

- Uses MySQL (see `docker-compose.yml` for credentials)
- Default DB: `buddydb`
- Default user: `buddyuser` / `buddypass`
- Data is initialized from `data.sql` if present

---

## Project Structure

```
productbuddy/
  api/                # Django app with models, views, serializers, migrations
  db.sqlite3          # (if using SQLite for dev)
  docker-compose.yml  # Docker setup for API and MySQL
  productbuddy/       # Django project settings
  data.sql            # Initial DB data (optional)
  Dockerfile
  README.md
  manage.py
  mysql-volume.tar.gz  #backup file
  products.csv
  requirement.txt
  tfidf_matrix.npz
  tfidf_vectorizer.pkl
order.py
product_recommender.py
product.py
```
---
## Google Colab file for data processcing and Cleaning
```
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/16O0A4dlzYiGgwRoHeL6eq6jeuNtrXWEH?usp=sharing)
```
---
---
## Contact
- email: vanshrastogi212@gmail.com 
---
