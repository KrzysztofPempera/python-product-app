from sqlalchemy import String
from models.base import Base, Column
class Product(Base):
    __tablename__ = "product"

    marker = Column(String(length=10))
    model = Column(String(length=50), primary_key=True, index=True)
    type = Column(String(length=50))
    
    __mapper_args__ = {
        'polymorphic_on': type,
        'polymorphic_identity': 'product',
        'with_polymorphic': '*'
    }
