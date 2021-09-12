"""
Name: Eton Cheng
interest.py

Problem: calculate the monthly interest charge

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

# annual interest rate = 0.1584
# number of days = 31
# net balance = 850
# payment amount = 400
# remain days = 11
# months = 12


def main():
    print("This program calculates the monthly interest charge")
    annual_interest_rate = eval(input("Enter the annual interest rate: "))
    number_of_days = eval(input("Enter the number of days in billing cycle: "))
    net_balance = eval(input("Enter the net balance: "))
    payment_amount = eval(input("Enter the payment amount: "))
    remain_days = eval(input("Enter the remaining days: "))
    months = eval(input("Enter the number of months: "))
    average_daily_balance = ((net_balance * number_of_days) - (payment_amount * remain_days)) / number_of_days
    monthly_interest_rate = annual_interest_rate / months
    monthly_interest_charge = average_daily_balance * monthly_interest_rate
    print("monthly interest charge: $", round(monthly_interest_charge, 2))


main()

