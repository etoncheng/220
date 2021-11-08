"""
Name: Eton Cheng
salesforce.py

Problem: encapsulates data for a sales person

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


def salesforce():
    sales_people = input("Enter names of the salespeople: ")
    employee_id = input("Enter their ID numbers: ")
    sale_amount = input("Enter their sale amount: ")
    print(sales_people)
    print(employee_id)
    print(sale_amount)


class Salesforce:
    def __init__(self, sales_people):
        self.people = sales_people

    def add_data(self, file_name):
        self.file_name = file_name
        file_name = "salespeople.txt"
        file = open(file_name, 'r')
        file.readline()
        sales_people = file.readline()
        employee_id, name, sale_amount = sales_people.split(",")

    def quota_report(self, quota):
        self.quota = quota
        if self.people == self.quota:
            return True
        else:
            return False

    def top_seller(self):
        return self.people

    def individual_sales(self, employee_id):
        self.employee_id = employee_id
        if self.people == self.employee_id:
            return Salesforce
        else:
            return None
