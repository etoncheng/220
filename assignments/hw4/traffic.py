"""
Name: Eton Cheng
traffic.py

Problem: surveying roads

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


def main():
    roads = eval(input("How many roads were surveyed: "))

    road1 = eval(input("How many days was Road 1 surveyed: "))
    total = 0
    for i in range(1, road1 + 1):
        road1 = eval(input("How many cars traveled on day: "))
        total = road1 + total
    road1_average = total / road1
    print("Road 1 average vehicles per day is", round(road1_average, 1))

    road2 = eval(input("How many days was Road 2 surveyed: "))
    total = 0
    for i in range(1, road2 + 1):
        road2 = eval(input("How many cars traveled on day: "))
        total = road2 + total
    road2_average = total / road2
    print("Road 2 average vehicles per day is", round(road2_average, 1))

    road3 = eval(input("How many days was Road 3 surveyed: "))
    total = 0
    for i in range(1, road3 + 1):
        road3 = eval(input("How many cars traveled on day: "))
        total = road3 + total
    road3_average = total / road3
    print("Road 3 average vehicles per day is", round(road3_average, 1))

    total_number_vehicles = eval(input("Total number of vehicles traveled on all roads: "))
    average_number_vehicles = total_number_vehicles / roads
    print("Average number of vehicles per road is", round(average_number_vehicles, 2))


main()
