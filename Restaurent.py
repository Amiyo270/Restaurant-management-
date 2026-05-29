from Menu import menu

class Restaurent:
    def __init__(self, name):
        self.name = name
        self.employees = []
        self.menu = menu()

    def add_employee(self, employee):
        self.employees.append(employee)

    def view_employee(self):
        print("\nEmployees List : ")
        if not self.employees:
            print("No employees found.")
            return
        for emp in self.employees:
            print(f"Name: {emp.name} | Email: {emp.email} | Phone: {emp.phone} | Address: {emp.address} | Designation: {emp.designation}")