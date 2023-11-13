from fastapi import HTTPException

def calculate_profitability_index(product):
    if product.price == 0:
        raise HTTPException(status_code=400, detail="Product price cannot be zero")

    index = (product.ram + product.hd)/product.price*product.speed
    rounded_index = round(index, 2)

    return rounded_index