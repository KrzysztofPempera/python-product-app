from fastapi import HTTPException
from sqlalchemy.orm import Session
from models.product import Product

def get_product_by_model(db: Session, model: str):
    product = db.query(Product).filter_by(model=model).first()

    if not product:
        raise HTTPException(status_code=404, detail=f"Product with model {model} not found")

    return product

            