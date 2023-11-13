from sqlalchemy import Integer, ForeignKey, String, Float
from sqlalchemy.orm import relationship
from models.base import Base, Column

class Laptop(Base):
    __tablename__ = "laptop"

    code = Column(Integer, primary_key=True)
    model = Column(String(length=50), ForeignKey('product.model'), index=True)
    speed = Column(Integer)
    ram = Column(Integer)
    hd = Column(Integer)
    price = Column(Float(precision=2), nullable=True)
    screen = Column(Integer)

    product = relationship("Product", back_populates="laptop")