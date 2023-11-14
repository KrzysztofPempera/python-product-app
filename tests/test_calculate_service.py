import pytest
from fastapi import HTTPException
from models.pc import PcProduct
from models.laptop import LaptopProduct
from service.calculate_service import calculate_profitability_index


def test_calculate_profitability_index_pc_product():
    #Arrange
    product = PcProduct(ram=8, hd=512, price=100, speed=3)
    expected_result = 15.60

    #Act
    result = calculate_profitability_index(product)

    #Assert
    assert result == expected_result

def test_calculate_profitability_index_laptop_product():
    #Arrange
    product = LaptopProduct(ram=8, hd=512, price=100, speed=3)
    expected_result = 15.60

    #Act
    result = calculate_profitability_index(product)

    #Assert
    assert result == expected_result

def test_calculate_profitability_index_with_price_zero_throws_exception():
    #Arrange
    product = PcProduct(ram=8, hd=512, price=0, speed=3)
    expected_exception_code = 400
    expected_exception_detail = "Product price cannot be zero"

    #Act
    with pytest.raises(HTTPException) as exc_info:
        calculate_profitability_index(product)

    #Assert
    assert exc_info.value.status_code == expected_exception_code
    assert exc_info.value.detail == expected_exception_detail

def test_calculate_profitability_index_with_printer_product_throws_exception():
    #Arrange
    product = PcProduct(ram=8, hd=512, price=0, speed=3, type='printer')
    expected_exception_code = 400
    expected_exception_detail = "Cannot calculate profitability index of products other than pc and laptop"

    #Act
    with pytest.raises(HTTPException) as exc_info:
        calculate_profitability_index(product)

    #Assert
    assert exc_info.value.status_code == expected_exception_code
    assert exc_info.value.detail == expected_exception_detail