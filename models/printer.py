from sqlalchemy import Integer, ForeignKey, String, Float
from models.base import Column
from models.product import Product

class PrinterProduct(Product):
    __tablename__ = "printer"
    
    code = Column(Integer, primary_key=True)
    model = Column(String(length=50), ForeignKey('product.model'), index=True)
    color = Column(String(length=1))
    printer_type = Column(String(length=10))
    price = Column(Float(precision=2), nullable=True)

    __mapper_args__ = {
        'polymorphic_identity': 'printer',
    }