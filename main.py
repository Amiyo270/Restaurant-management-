from FoodItems import FoodItem
from Users import customer as CustomerClass, admin as AdminClass, employee as EmployeeClass
from Restaurent import Restaurent

amiyo_restaurent = Restaurent("Amiyo Restaurent")

def customer_menu():
    name = input("Enter your Name : ")
    email = input("Enter your Email : ")
    phone = input("Enter your Number : ")
    address = input("Enter your Address : ")
    
    # Avoid shadowing the class token name by using a unique variable name
    active_customer = CustomerClass(name=name, phone=phone, email=email, address=address)

    while True:
        print(f"\nWelcome {active_customer.name} !!")
        print("1. View Menu")
        print("2. Add Item to Cart")
        print("3. View Cart")
        print("4. Pay Bill")
        print("5. Exit")

        try:
            choice = int(input("Enter Your Choice: "))
        except ValueError:
            print("Invalid Input! Please enter a number.")
            continue

        if choice == 1:
            active_customer.view_menu(amiyo_restaurent)
        elif choice == 2:
            item_name = input("Enter item name : ")
            try:
                item_quantity = int(input("Enter item quantity : "))
                active_customer.add_to_cart(amiyo_restaurent, item_name, item_quantity)
            except ValueError:
                print("Invalid quantity format.")
        elif choice == 3:
            active_customer.view_cart()
        elif choice == 4:
            active_customer.pay_bill()
        elif choice == 5:
            break
        else:
            print("Invalid Input")


def admin_menu():
    name = input("Enter your Name : ")
    email = input("Enter your Email : ")
    phone = input("Enter your Number : ")
    address = input("Enter your Address : ")
    
    active_admin = AdminClass(name=name, phone=phone, email=email, address=address)

    while True:
        print(f"\nWelcome Admin {active_admin.name} !!")
        print("1. Add new item")
        print("2. Add new Employee")
        print("3. View Employee")
        print("4. View Items")
        print("5. Delete Item")
        print("6. Exit")

        try:
            choice = int(input("Enter Your Choice: "))
        except ValueError:
            print("Invalid Input! Please enter a number.")
            continue

        if choice == 1:
            item_name = input("Enter Item name : ")
            try:
                item_price = int(input("Enter Item price : "))
                item_quantity = int(input("Enter Item quantity : "))
                new_item = FoodItem(item_name, item_price, item_quantity)
                active_admin.add_new_item(amiyo_restaurent, new_item)
            except ValueError:
                print("Invalid input values for price or quantity.")

        elif choice == 2:
            emp_name = input("Enter employee name : ")
            emp_phone = input("Enter employee phone : ")
            emp_email = input("Enter employee email : ")
            emp_designation = input("Enter employee designation : ")
            emp_age = input("Enter employee Age : ")
            emp_salary = input("Enter employee Salary : ")
            emp_address = input("Enter employee address : ")
            
            # Instantiating the object before sending it to administration
            new_emp = EmployeeClass(emp_name, emp_phone, emp_email, emp_address, emp_age, emp_designation, emp_salary)
            active_admin.add_employee(amiyo_restaurent, new_emp)
            
        elif choice == 3:
            active_admin.view_employee(amiyo_restaurent)
        elif choice == 4:
            active_admin.view_menu(amiyo_restaurent)
        elif choice == 5:
            item_name = input("Enter item name : ")
            active_admin.remove_item(amiyo_restaurent, item_name)
        elif choice == 6:
            break
        else:
            print("Invalid Input")


if __name__ == "__main__":
    while True:
        print("\n--- WELCOME ---")
        print("1. Customer")
        print("2. Admin")
        print("3. Exit")
        try:
            choice = int(input("Enter your choice : "))
        except ValueError:
            print("Please enter a valid numeric choice.")
            continue

        if choice == 1:
            customer_menu()
        elif choice == 2:
            admin_menu()
        elif choice == 3:
            print("Goodbye!")
            break
        else:
            print("Invalid Input !! ")