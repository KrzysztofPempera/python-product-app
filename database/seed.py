import logging
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.base import Base
from models.printer import PrinterProduct
from models.pc import PcProduct
from models.laptop import LaptopProduct

logging.basicConfig(filename='database_seed.log', level=logging.ERROR)

def seed_database():
    engine = create_engine('sqlite:///inpost.db')

    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    try:
        pc = PcProduct(marker='M1', type='pc', code=1, model='pc-model', speed=2000, ram=8, hd=512, cd='DVD', price=899.99)
        pc2 = PcProduct(marker='M11', type='pc', code=2, model='pc-model2', speed=4000, ram=8, hd=1024, cd='DVD', price=399.99)
        pc3 = PcProduct(marker='M111', type='pc', code=3, model='pc-model3', speed=1000, ram=4, hd=256, cd='DVD', price=699.99)

        laptop = LaptopProduct(marker='M2', type='laptop',code=4, model='laptop-model', speed=2500, ram=16, hd=1024, price=1299.99, screen=15)
        laptop2 = LaptopProduct(marker='M22', type='laptop',code=5, model='laptop-model2', speed=100, ram=16, hd=2048, price=799.99, screen=14)
        laptop3 = LaptopProduct(marker='M222', type='laptop',code=6, model='laptop-model3', speed=42, ram=32, hd=2048, price=299.99, screen=12)
        
        printer = PrinterProduct(marker='M3', type='printer',code=7, model='printer-model', color='Y', printer_type='Laser', price=199.99)
        printer2 = PrinterProduct(marker='M33', type='printer',code=8, model='printer-model2', color='Y', printer_type='Laser', price=2299.99)
        printer3 = PrinterProduct(marker='M333', type='printer',code=9, model='printer-model3', color='Y', printer_type='Laser', price=299.99)

        session.add_all([pc, laptop, printer, pc2, laptop2, printer2, pc3, laptop3, printer3])
        session.commit()
    except Exception as e:
        logging.error(f'Error seeding database: {e}')
        session.rollback()
    finally:
        session.close()
        engine.dispose()

