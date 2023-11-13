from sqlalchemy import Integer, ForeignKey, String, Float
from models.base import Column
from models.product import Product

class LaptopProduct(Product):
    __tablename__ = "laptop"

    code = Column(Integer, primary_key=True)
    model = Column(String(length=50), ForeignKey('product.model'), index=True)
    speed = Column(Integer)
    ram = Column(Integer)
    hd = Column(Integer)
    price = Column(Float(precision=2), nullable=True)
    screen = Column(Integer)

    __mapper_args__ = {
        'polymorphic_identity': 'laptop',
    }