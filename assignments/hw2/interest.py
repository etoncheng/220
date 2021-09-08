"""
Name: Eton Cheng
interest.py

Problem: write a program displaying monthly interest charge

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""
# net balance = 850
# number of days = 31
# payment amount = 400
# remaining days = 11
# step 1 result = 26350
# step 2 result = 4400
# step 3 result = 21950
# step 4 result = 708.06
# annual percentage rate = 0.1584
# monthly interest rate = 0.0132
# number of months = 12


def calc_step_1():
    net_balance = eval(input("Enter the net balance: "))
    number_of_days = eval(input("Enter the number of days: "))
    step_1 = net_balance * number_of_days
    print("Step_1 =", step_1)


calc_step_1()


def calc_step_2():
    payment_amount = eval(input("Enter the payment amount: "))
    remaining_days = eval(input("Enter the remaining days: "))
    step_2 = payment_amount * remaining_days
    print("Step_2 =", step_2)


calc_step_2()


def calc_step_3():
    step_1 = eval(input("Enter Step 1 Result: "))
    step_2 = eval(input("Enter Step 2 Result: "))
    step_3 = step_1 - step_2
    print("Step_3 =", step_3)


calc_step_3()


def calc_step_4():
    step_3 = eval(input("Enter Step 3 Result: "))
    number_of_days = eval(input("Enter the number of days: "))
    step_4 = step_3 / number_of_days
    print("Step_4 =", step_4)


calc_step_4()


def calc_monthly_interest_rate():
    annual_percentage_rate = eval(input("Enter the annual percentage rate: "))
    number_of_months = eval(input("Enter the number of months: "))
    monthly_interest_rate = annual_percentage_rate / number_of_months
    print("Monthly_Interest_Rate =", monthly_interest_rate)


calc_monthly_interest_rate()


def calc_monthly_interest_charge():
    step_4 = eval(input("Enter Step 4 Result: "))
    monthly_interest_rate = eval(input("Enter the monthly interest rate: "))
    monthly_interest_charge = step_4 * monthly_interest_rate
    print("Monthly_Interest_Charge =", monthly_interest_charge)


calc_monthly_interest_charge()
