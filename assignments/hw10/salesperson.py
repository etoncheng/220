"""
Name: Eton Cheng
salesperson.py

Problem: encapsulates data for a sales person

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


def salesperson():
    employee_id = input("Enter employee_id: ")
    name = input("Enter name: ")
    sales = input("Enter sales: ")
    print(employee_id)
    print(name)
    print(sales)


class Salesperson:
    def __init__(self, employee_id, name, sales):
        self.id = employee_id
        self.name = name
        self.sales = sales

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def enter_sales(self, sales):
        self.sales = sales

    def total_sales(self):
        total = sum(self.sales)

    def get_sales(self):
        return self.sales

    def met_quota(self, quota):
        self.quota = quota
        if self.sales >= self.quota:
            return True
        else:
            return False

    def compare_to(self, other):
        self.other = other
        if self.other > self.sales:
            return -1
        if self.other < self.sales:
            return 1
        if self.other == self.sales:
            return 0

    def __str__(self):
        return self.id, self.name, self.sales
