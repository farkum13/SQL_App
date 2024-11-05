import requests

from app.config.db import SessionLocal
from app.controllers.productControllers import create_product


# Fetch products from FakeStore API and insert into database
def fetch_and_store_products():
    url = "https://fakestoreapi.com/products"
    response = requests.get(url)
    products = response.json()

    db = SessionLocal()

    try:
        for product in products:
            create_product(db, product)
    except Exception:
        db.rollback()
        raise
    finally:
        db.close()

if __name__ == "__main__":
    fetch_and_store_products()