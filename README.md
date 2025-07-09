# 🛒 Shopping Cart System (Python OOP Project)

This project is a **console-based Shopping Cart System** implemented in Python using Object-Oriented Programming (OOP). It allows customers to add products to a cart, remove items, view the cart, and proceed to checkout.

---

## ✅ Features

- Add predefined products to a store
- Add or remove items from the shopping cart
- View items in the cart with individual and total prices
- Checkout and clear the cart
- Handles invalid inputs gracefully

---

## 🧱 Class Overview

### `Product`
Represents a product in the store.
- Attributes: `product_id`, `name`, `price`
- Method: `__str__()` for string representation

### `Cartitem`
Wraps a product with quantity for the cart.
- Attributes: `product`, `quantity`
- Method: `get_total()` calculates total price of the item

### `Cart`
Handles all cart operations.
- Methods:
  - `add_items(product, quantity)`: Adds item or increases quantity
  - `remove_item(product_id)`: Removes item by ID
  - `view_cart()`: Displays cart contents
  - `calculate_total()`: Calculates total price
  - `checkout()`: Completes purchase and clears the cart

### `Store`
Maintains the product list.
- Methods:
  - `add_product(product)`: Adds a product to the store
  - `show_products()`: Displays all products
  - `get_product_by_id(product_id)`: Fetches a product by its ID

---

## 🧪 Sample Execution

```python
store = Store()
store.add_product(Product(1, "Laptop", 1000))
store.add_product(Product(2, "Mouse", 25))
store.add_product(Product(3, "Keyboard", 45))

cart = Cart()

while True:
    store.show_products()
    print("\n1. Add to Cart\n2. Remove from Cart\n3. View Cart\n4. Checkout\n5. Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        pid = int(input("Enter Product ID: "))
        qty = int(input("Enter quantity: "))
        product = store.get_product_by_id(pid)
        if product:
            cart.add_items(product, qty)
        else:
            print("Product not found.")
    elif choice == "2":
        pid = int(input("Enter Product ID to remove: "))
        cart.remove_item(pid)
    elif choice == "3":
        cart.view_cart()
    elif choice == "4":
        cart.checkout()
    elif choice == "5":
        break
