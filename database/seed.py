from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.base import Base
from models.product import Product
from models.printer import Printer
from models.pc import Pc
from models.laptop import Laptop

def seed_database():
    engine = create_engine('sqlite:///inpost.db', echo=True)

    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    try:
        product1 = Product(marker='M1', model='model1', type='pc')
        product2 = Product(marker='M2', model='model2', type='laptop')
        product3 = Product(marker='M3', model='model3', type='printer')

        session.add_all([product1, product2, product3])
        session.commit()

        pc = Pc(code=1, model='model1', speed=2000, ram=8, hd=512, cd='DVD', price=899.99)
        laptop = Laptop(code=2, model='model2', speed=2500, ram=16, hd=1024, price=1299.99, screen=15)
        printer = Printer(code=3, model='model3', color='Y', type='Laser', price=199.99)

        session.add_all([pc, laptop, printer])
        session.commit()
    except Exception as e:
        print(f'Error seeding database: {e}')
        session.rollback()
    finally:
        session.close()
        engine.dispose()

