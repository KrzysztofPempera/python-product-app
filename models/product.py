from sqlalchemy import String
from sqlalchemy.orm import relationship
from models.base import Base, Column

class Product(Base):
    __tablename__ = "product"

    marker = Column(String(length=10))
    model = Column(String(length=50), primary_key=True, index=True)
    type = Column(String(length=50))

    pc = relationship("Pc", uselist=False, back_populates="product")
    laptop = relationship("Laptop", uselist=False, back_populates="product")
    printer = relationship("Printer", uselist=False, back_populates="product")
