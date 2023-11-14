from fastapi import APIRouter, Depends, Query
from fastapi.responses import FileResponse
from sqlalchemy.orm import Session
from service.calculate_service import calculate_profitability_index
from service.csv_service import create_index_csv
from repository.product import get_product_by_model
from database.connection import get_db
from typing import Annotated

router = APIRouter()

@router.get("/index")
async def calculate_index(model: Annotated[str, Query(max_length=50)], db: Session = Depends(get_db)):
    product = get_product_by_model(db=db, model=model)
    index = calculate_profitability_index(product=product)
    create_index_csv(product=product, index=index)

    try:
        return FileResponse('index.csv', filename='profitability_indexes.csv', media_type="text/csv")
    except FileNotFoundError:
        return {"error": "File not found"}