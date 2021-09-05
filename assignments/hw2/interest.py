"""
Name: Eton Cheng
interest.py

Problem: this program illustrates a monthly interest function

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


def calc_step_1():
    net_balance = 850
    number_of_days = 31
    step_1 = net_balance * number_of_days
    print("Step_1 =", step_1)


def calc_step_2():
    payment_amount = 400
    remaining_days = 11
    step_2 = payment_amount * remaining_days
    print("Step_2 =", step_2)


def calc_step_3():
    step_1 = 26350
    step_2 = 4400
    step_3 = step_1 - step_2
    print("Step_3 =", step_3)


def calc_step_4():
    step_3 = 21950
    number_of_days = 31
    step_4 = step_3 / number_of_days
    print("Step_4 =", step_4)


def calc_monthly_interest_rate():
    annual_percentage_rate = 0.1584
    number_of_months = 12
    monthly_interest_rate = annual_percentage_rate / number_of_months
    print("Monthly_Interest_Rate =", monthly_interest_rate)


def calc_monthly_interest_charge():
    step_4 = 708.06
    monthly_interest_rate = 0.0132
    monthly_interest_charge = step_4 * monthly_interest_rate
    print("Monthly_Interest_Charge =", monthly_interest_charge)


calc_monthly_interest_charge()
