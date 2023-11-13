from sqlalchemy import Integer, ForeignKey, String, Float
from sqlalchemy.orm import relationship
from models.base import Base, Column
class Pc(Base):
    __tablename__ = "pc"

    code = Column(Integer, primary_key=True)
    model = Column(String(length=50), ForeignKey('product.model'), index=True)
    speed = Column(Integer)
    ram = Column(Integer)
    hd = Column(Integer)
    cd = Column(String(length=10))
    price = Column(Float(precision=2), nullable=True)

    product = relationship("Product", back_populates="pc")