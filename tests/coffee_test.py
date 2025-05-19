import pytest
from coffee import Coffee
from customer import Customer

def test_coffee_name_valid():
    c = Coffee("Espresso")
    assert c.name == "Espresso"

def test_coffee_name_too_short():
    with pytest.raises(ValueError):
        Coffee("AB")

def test_coffee_orders_and_customers():
    coffee = Coffee("Cappuccino")
    cust1 = Customer("Amy")
    cust2 = Customer("Max")

    cust1.create_order(coffee, 2.5)
    cust2.create_order(coffee, 3.0)

    assert len(coffee.orders()) == 2
    assert set(coffee.customers()) == {cust1, cust2}

def test_average_price():
    coffee = Coffee("Mocha")
    cust1 = Customer("Jan")
    cust1.create_order(coffee, 4.0)
    cust1.create_order(coffee, 6.0)

    assert coffee.average_price() == 5.0

def test_num_orders():
    coffee = Coffee("Americano")
    assert coffee.num_orders() == 0

    cust = Customer("Ben")
    cust.create_order(coffee, 3.0)

    assert coffee.num_orders() == 1
