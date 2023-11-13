from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column as BaseColumn, Integer, String, ForeignKey, Float
from sqlalchemy.orm import relationship

Base = declarative_base()

class Column(BaseColumn):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('nullable', False)
        super().__init__(*args, **kwargs)

class Product(Base):
    __tablename__ = "product"

    marker = Column(String(length=10))
    model = Column(String(length=50), primary_key=True, index=True)
    type = Column(String(length=50))

    pc = relationship("Pc", uselist=False, back_populates="product")
    laptop = relationship("Laptop", uselist=False, back_populates="product")
    printer = relationship("Printer", uselist=False, back_populates="product")

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

class Printer(Base):
    __tablename__ = "printer"
    
    code = Column(Integer, primary_key=True)
    model = Column(String(length=50), ForeignKey('product.model'), index=True)
    color = Column(String(length=1))
    type = Column(String(length=10))
    price = Column(Float(precision=2), nullable=True)

    product = relationship("Product", back_populates="printer")