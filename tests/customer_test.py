import pytest
from customer import Customer
from coffee import Coffee
from order import Order

def test_customer_name_valid():
    c = Customer("Alice")
    assert c.name == "Alice"

def test_customer_name_too_long():
    with pytest.raises(ValueError):
        Customer("A_very_long_name_exceeding_15")

def test_customer_name_not_string():
    with pytest.raises(ValueError):
        Customer(123)

def test_customer_orders_and_coffees():
    c = Customer("Bob")
    coffee = Coffee("Latte")
    c.create_order(coffee, 3.5)
    assert len(c.orders()) == 1
    assert coffee in c.coffees()
