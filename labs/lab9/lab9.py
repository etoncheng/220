"""
Name: Eton Cheng
lab9.py

Problem: Conditionals

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""
from graphics import *
import math


def add_ten():
    list = [5, 2, -3]
    for n in range(len(list)):
        list[n] += 10
    print(list)


def square_each():
    list = [3, 5.7, 2]
    for n in range(len(list)):
        list[n] **= 2
    print(list)


def sum_list():
    list = [3, 5.7, 2]
    sum(list)
    print(sum)


def to_numbers():
    str_list = ['3', '5.7', '2']
    to_numbers = [int(n) for n in str_list]
    return to_numbers


def write_sum_of_squares():
    in_file_name = input("numbers in each line")
    out_file_name = input("the sum of squares")

    in_file = open(in_file_name, 'r')
    out_file = open(out_file_name, 'w')

    for list in in_file:
        list = [3, 5.7, 2]
        for n in range(len(list)):
            list[n] **= 2
        sum(list)
        print(list, file=out_file)

    in_file.close()
    out_file.close()


def starter():
    weight = eval(input("Enter the weight: "))
    num_wins = input("Enter the number of matches win: ")
    print("Weight in pounds:", weight)
    print("Number of matches win:", num_wins)
    if (weight >= 150 or weight < 160) and (num_wins >= 5):
        print("You should start")
    else:
        print("You should not start")
    if (weight > 199) and (num_wins > 20):
        print("You should start")
    else:
        print("You should not start")


def leap_year(year):
    if year % 4 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 400 == 0:
        return True
    else:
        return False
print(leap_year)


def circle_overlap():
    win = GraphWin("Draw 2 Circles", 700, 500)
    message = Text(Point(350, 450), "Click on two points")
    message.draw(win)

    p1 = win.getMouse()
    p1.draw(win)
    p2 = win.getMouse()
    p2.draw(win)

    circle1 = Circle(Point(p1, p2), 10)
    circle1.setFill("blue")
    circle1.draw(win)

    circle2 = Circle(Point(4, 5), 10)
    circle2.setFill("red")
    circle2.draw(win)

    x1, x2, y1, y2, r1, r2 = [float(i) for i in input().split()]
    d = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

    if (d < r2 - r1) or (d > r2 + r1):
        print("The circles overlap")
    else:
        print("The circles do not overlap")

    message.setText("Click anywhere to close")
    win.getMouse()
