from fastapi import APIRouter, Depends
from fastapi.responses import StreamingResponse
from sqlalchemy.orm import Session
from service.csv_service import create_deal_csv
from repository.product import get_random_product_by_type
from database.connection import get_db

router = APIRouter()

@router.get("/deal")
async def create_deals(db: Session = Depends(get_db)):
    pc_product = get_random_product_by_type(db=db, type='pc')
    laptop_product = get_random_product_by_type(db=db, type='laptop')
    printer_product = get_random_product_by_type(db=db, type='printer')
    
    csv_data = create_deal_csv(product1=pc_product, product2=printer_product)
    csv_data = create_deal_csv(product1=laptop_product, product2=printer_product, csv_data=csv_data)

    csv_data.seek(0)

    try:
        return StreamingResponse(iter([csv_data.getvalue()]), media_type="text/csv")
    except FileNotFoundError:
        return {"error": "Could not create file"}