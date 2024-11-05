
from sqlalchemy import Column, Integer, String, Float, Text
from app.config.db import Base

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    price = Column(Float)
    description = Column(Text)
    category = Column(String)
    image = Column(String)
    rating_rate = Column(Float)
    rating_count = Column(Integer)
