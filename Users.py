from abc import ABC
from Orders import order

class user(ABC):
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

class customer(user):
    def __init__(self, name, phone, email, address):
        super().__init__(name, phone, email, address)
        self.cart = order()

    def view_menu(self, restaurent):
        restaurent.menu.show_menu()

    def add_to_cart(self, restaurent, item_name, quantity):
        item = restaurent.menu.find_item(item_name)
        if item:
            if quantity > item.quantity:
                print("Item Quantity Exceeded !!")
            else:
                self.cart.add_item(item, quantity)
                item.quantity -= quantity  # Deduct stock from main menu
                print("Item Added to Cart")
        else:
            print("Item Not Found")

    def view_cart(self):
        print("\n--- View Cart ---")
        if not self.cart.items:
            print("Your cart is empty.")
            return
        print("Name\tPrice\tQuantity")
        for item, qty in self.cart.items.items():
            print(f"{item.name}\t{item.price}\t{qty}")
        print(f"Total Price : {self.cart.total_price}")

    def pay_bill(self):
        if not self.cart.items:
            print("Your cart is empty. Nothing to pay.")
            return
        print(f"Total {self.cart.total_price} paid successfully")
        self.cart.clear()


class employee(user):
    def __init__(self, name, phone, email, address, age, designation, salary):
        super().__init__(name, phone, email, address)
        self.age = age
        self.designation = designation 
        self.salary = salary


class admin(user):
    def __init__(self, name, phone, email, address):
        super().__init__(name, phone, email, address)

    def add_employee(self, restaurent, emp_obj):
        restaurent.add_employee(emp_obj)
        print("Employee added successfully!")

    def view_employee(self, restaurent):
        restaurent.view_employee()

    def add_new_item(self, restaurent, item):
        restaurent.menu.add_menu_item(item)
        print("Item added to menu successfully!")

    def remove_item(self, restaurent, item_name):
        restaurent.menu.remove_item(item_name)        

    def view_menu(self, restaurent):
        restaurent.menu.show_menu()