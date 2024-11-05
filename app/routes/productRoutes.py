from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.config.db import get_db
from app.schemas.product import ProductResponse
from app.controllers.productControllers import get_all_products,get_product_by_id,create_product

router = APIRouter()

# Get all products
@router.get("/products", response_model=list[ProductResponse])
def get_products(db: Session = Depends(get_db)):
    return get_all_products(db)

# Get a product by ID
@router.get("/products/{product_id}", response_model=ProductResponse)
def get_product(product_id: int, db: Session = Depends(get_db)):
    product = get_product_by_id(product_id, db)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

@router.post("/products", response_model=ProductResponse)
def add_product(product_data: ProductResponse, db: Session = Depends(get_db)):
    # Prepare the product data to match the expected structure
    product_dict = {
        "id": product_data.id,
        "title": product_data.title,
        "price": product_data.price,
        "description": product_data.description,
        "category": product_data.category,
        "image": product_data.image,
        "rating": {
            "rate": product_data.rating_rate,
            "count": product_data.rating_count
        }
    }
    return create_product(db, product_dict)