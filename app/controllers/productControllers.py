from sqlalchemy.orm import Session
from app.models.product import Product
from app.schemas.product import ProductResponse  # Ensure this line is included


# Get all products
def get_all_products(db: Session):
    return db.query(Product).all()


# Get a product by its ID
def get_product_by_id(product_id: int, db: Session):
    return db.query(Product).filter(Product.id == product_id).first()


def create_product(db: Session, product_data: dict):
    new_product = Product(
        id=product_data["id"],
        title=product_data["title"],
        price=product_data["price"],
        description=product_data["description"],
        category=product_data["category"],
        image=product_data["image"],
        rating_rate=product_data["rating"]["rate"],
        rating_count=product_data["rating"]["count"]
    )
    db.add(new_product)
    db.commit()
    db.refresh(new_product)

    # Create a ProductResponse instance to return
    return ProductResponse(
        id=new_product.id,
        title=new_product.title,
        price=new_product.price,
        description=new_product.description,
        category=new_product.category,
        image=new_product.image,
        rating_rate=new_product.rating_rate,
        rating_count=new_product.rating_count
    )
