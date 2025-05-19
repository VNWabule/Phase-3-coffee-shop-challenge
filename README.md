# ☕ Coffee Shop Challenge

A simple object-oriented Python application that simulates a coffee shop's order system. The project includes models for `Customer`, `Coffee`, and `Order`, and supports relationships, data validation, and basic business logic.

---

## 📁 Project Structure

coffee-shop-challenge/
├── Pipfile
├── Pipfile.lock
├── debug.py
├── customer.py
├── coffee.py
├── order.py
└── tests/
├── customer_test.py
├── coffee_test.py
└── order_test.py


---

## ✅ Requirements

### Models

- **Customer**
  - Must have a name (string, 1–15 characters).
  - Can create orders.
  - Can retrieve their unique coffees ordered.

- **Coffee**
  - Must have a name (string, at least 3 characters).
  - Immutable once created.
  - Can calculate number of orders and average price.

- **Order**
  - Linked to a `Customer` and a `Coffee`.
  - Price must be a float between 1.0 and 10.0.
  - Immutable after creation.

---

## 🔗 Relationships

- A `Customer` can have many `Orders`.
- A `Coffee` can be associated with many `Orders`.
- `Order` connects `Customer` and `Coffee`.

---

## 📊 Aggregates & Methods

- `Customer.create_order(coffee, price)`  
- `Customer.coffees()`  
- `Coffee.customers()`  
- `Coffee.num_orders()`  
- `Coffee.average_price()`  
- `Customer.most_aficionado(coffee)`

---

## ⚙️ Setup Instructions

1. **Clone the repository**
   ```bash
   git clone git@github.com:VNWabule/Phase-3-coffee-shop-challenge.git

2. **Initialize pipenv environment**
   ```bash
   pipenv install
   pipenv shell

3. **If you haven't already install pytest**
   ```bash
   pipenv install pytest

4. **Run tests using pytest**
   ```bash
   pytest



