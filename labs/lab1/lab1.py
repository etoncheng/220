"""
Name: Eton Cheng
lab1.py
"""


def calc_area():
    length = 20
    width = 5
    area = length * width
    print("Area =", area)


calc_area()


def calc_rec_area():
    length = eval(input("Enter the length: "))
    width = eval(input("Enter the width: "))
    area = length * width
    print("Area =", area)


calc_rec_area()


def calc_rec_volume():
    height = eval(input("Enter the height: "))
    width = eval(input("Enter the width: "))
    length = eval(input("Enter the length: "))
    volume = height * width * length
    print("Volume =", volume)


calc_rec_volume()


def shooting_percentage():
    shot = eval(input("Enter the shot: "))
    total = eval(input("Enter the total: "))
    percentage = shot / total
    print("Percentage =", percentage)


shooting_percentage()


def coffee_total_cost():
    coffee_per_pound = 10.50
    shipping_costs_per_pound = 0.86
    fixed_cost = 1.50
    pound = eval(input("Enter the pound: "))
    total_cost = (coffee_per_pound * pound) + (shipping_costs_per_pound * pound) + fixed_cost
    print("Total_cost =", total_cost)


coffee_total_cost()


def kilometers_to_miles():
    kilometer = eval(input("Enter the kilometer: "))
    mile = kilometer / 1.61
    print("Mile =", mile)


kilometers_to_miles()