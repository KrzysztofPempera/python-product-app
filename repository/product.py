from sqlalchemy.orm import Session
from models.product import Product

def get_product_by_model(db: Session, model: str):
    return db.query(Product).filter_by(model=model).first()

            