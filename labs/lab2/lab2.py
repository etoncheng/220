"""
Name: Eton Cheng
lab2.py
"""
import math


def sum_of_threes():
    bound = eval(input("Enter an upper bound: "))
    total = 0
    for threes in range(3, bound + 1, 3):
        total = total + threes
        print(total)
    print("The total is: ", total)


sum_of_threes()


def multiplication_table():
    count = 1
    for multiples in range(1, 11):
        print(1*count, 2*count, 3*count, 4*count, 5*count, 6*count, 7*count, 8*count, 9*count, 10*count)
        count = count + 1


multiplication_table()


def triangle_area():
    a = eval(input("Enter the height: "))
    b = eval(input("Enter the width: "))
    c = eval(input("Enter the length: "))
    s = (a+b+c)/2
    area1 = s*(s-a)*(s-b)*(s-c)
    area = math.sqrt(area1)
    print(area)


triangle_area()


def sumSquares():
    lower = eval(input("Enter a lower bound: "))
    higher = eval(input("Enter a higher bound: "))
    sum = 0
    for squares in range(lower, higher):
        sum = sum + squares ^ 2
    print(sum)


sumSquares()


def power():
    base = eval(input("Enter a base: "))
    exponent = eval(input("Enter an exponent: "))
    answer = 1
    for powers in range(1, exponent + 1):
        answer = answer * base
    print(base, "^", exponent, "=", answer)


power()