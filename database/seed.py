from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.base import Base
from models.printer import PrinterProduct
from models.pc import PcProduct
from models.laptop import LaptopProduct

def seed_database():
    engine = create_engine('sqlite:///inpost.db', echo=True)

    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    try:
        pc = PcProduct(marker='M1', type='pc', code=1, model='model1', speed=2000, ram=8, hd=512, cd='DVD', price=899.99)
        laptop = LaptopProduct(marker='M2', type='laptop',code=2, model='model2', speed=2500, ram=16, hd=1024, price=1299.99, screen=15)
        printer = PrinterProduct(marker='M3', type='printer',code=3, model='model3', color='Y', printerType='Laser', price=199.99)

        session.add_all([pc, laptop, printer])
        session.commit()
    except Exception as e:
        print(f'Error seeding database: {e}')
        session.rollback()
    finally:
        session.close()
        engine.dispose()

