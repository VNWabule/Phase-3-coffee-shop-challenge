import pytest
from customer import Customer
from coffee import Coffee
from order import Order

def test_order_valid():
    cust = Customer("Tom")
    coffee = Coffee("Flat White")
    order = Order(cust, coffee, 4.5)

    assert order.customer == cust
    assert order.coffee == coffee
    assert order.price == 4.5

def test_order_invalid_price_type():
    cust = Customer("Sam")
    coffee = Coffee("Drip")
    with pytest.raises(ValueError):
        Order(cust, coffee, "cheap")

def test_order_invalid_price_range():
    cust = Customer("Eva")
    coffee = Coffee("Macchiato")
    with pytest.raises(ValueError):
        Order(cust, coffee, 12.0)

def test_order_invalid_customer():
    coffee = Coffee("Cold Brew")
    with pytest.raises(TypeError):
        Order("NotACustomer", coffee, 4.0)

def test_order_invalid_coffee():
    cust = Customer("Lily")
    with pytest.raises(TypeError):
        Order(cust, "NotACoffee", 4.0)
