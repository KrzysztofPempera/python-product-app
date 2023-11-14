from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from service.csv_service import create_deal_csv
from repository.product import get_product_by_type
from database.connection import get_db

router = APIRouter()

@router.get("/deal")
async def create_deals(db: Session = Depends(get_db)):
    pc_product = get_product_by_type(db=db, type='pc')
    laptop_product = get_product_by_type(db=db, type='laptop')
    printer_product = get_product_by_type(db=db, type='printer')
    
    create_deal_csv(product1=pc_product, product2=printer_product)
    create_deal_csv(product1=laptop_product, product2=printer_product)
