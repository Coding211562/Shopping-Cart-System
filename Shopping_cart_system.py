class Product:
    def __init__(self , product_id , name , price):
        self.product_id = product_id
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name} - Rs.{self.price:.2f}"  

class Cartitem:
    def __init__(self , product , quantity):
        self.product = product
        self.quantity =  quantity

    def get_total(self):
        return self.product.price*self.quantity

class Cart:
    def __init__(self):
        self.items = []

    def add_items(self , product , quantity):
        for item in self.items:
            if item.product.product_id == product.product_id:
                item.quantity += quantity
                return
        self.items.append(Cartitem(product, quantity))    

    def remove_item(self , product_id):
        self.items = [item for item in self.items if item.product.product_id != product_id]                      

    def view_cart(self):
        if not self.items:
            print("Your cart is empty.")
            return
        print("\nYour Cart:")
        for item in self.items:
            print(f"{item.product.name} x {item.quantity} - Rs.{item.get_total():.2f}") 
        print(f"Total: Rs.{self.calculate_total():.2f}")  

    def calculate_total(self):
        return sum(item.get_total() for item in self.items) 

    def checkout(self):
        total = self.calculate_total()
        if total == 0:
            print("Cart is empty! Cannot checkout.")
        else:
            print(f"Checkout successful! Total paid: Rs.{total:.2f}")
            self.items.clear()  

class Store:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def show_products(self):
        print("\nAvailable Products:")
        for p in self.products:
            print(f"{p.product_id}. {p.name} - Rs.{p.price:.2f}")  

    def get_product_by_id(self, product_id):
        for p in self.products:
            if p.product_id == product_id:
                return p
        return None
    


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
            cart.add_item(product, qty)
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
    else:
        None
