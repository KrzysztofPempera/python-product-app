from sqlalchemy import Integer, ForeignKey, String, Float
from models.base import Column
from models.product import Product

class PcProduct(Product):
    __tablename__ = "pc"

    code = Column(Integer, primary_key=True)
    model = Column(String(length=50), ForeignKey('product.model'), index=True)
    speed = Column(Integer)
    ram = Column(Integer)
    hd = Column(Integer)
    cd = Column(String(length=10))
    price = Column(Float(precision=2), nullable=True)

    __mapper_args__ = {
        'polymorphic_identity': 'pc',
    }