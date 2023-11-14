from fastapi import HTTPException
from models.pc import PcProduct
from models.laptop import LaptopProduct

def calculate_profitability_index(product):
    if type(product) != PcProduct and type(product) != LaptopProduct:
         raise HTTPException(status_code=400, detail="Cannot calculate profitability index of products other than pc or laptop")

    if product.price == 0:
        raise HTTPException(status_code=400, detail="Product price cannot be zero")

    index = (product.ram + product.hd)/product.price*product.speed
    rounded_index = round(index, 2)

    return rounded_index