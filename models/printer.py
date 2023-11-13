from sqlalchemy import Integer, ForeignKey, String, Float
from sqlalchemy.orm import relationship
from models.base import Base, Column

class Printer(Base):
    __tablename__ = "printer"
    
    code = Column(Integer, primary_key=True)
    model = Column(String(length=50), ForeignKey('product.model'), index=True)
    color = Column(String(length=1))
    type = Column(String(length=10))
    price = Column(Float(precision=2), nullable=True)

    product = relationship("Product", back_populates="printer")