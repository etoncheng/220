"""
Name: Eton Cheng
lab7.py

Problem: String Files Practice

Certification of Authenticity:
I certify that this assignment is entirely our my work.
"""


def cash_conversion():
    five = 5
    print('${:.2f}'.format(five))


def encode():
    message = input("Enter a message: ")
    cipher = input("Enter a cipher: ")
    encryption = ""
    for c in message:
        encryption = encryption + chr(ord(c) - 97)
    print(encryption)


def surface_area_and_volume():
    import math
    radius = float(input("Enter radius of a sphere"))
    surface_area = 4 * math.pi * pow(radius, 2)
    volume = (4/3) * math.pi * pow(radius, 3)
    print("The surface area of sphere is:", surface_area)
    print("The volume of sphere is:", volume)


def sum_n(n):
    n = eval(input("Enter a number: "))
    sum = 0
    for i in range(1, n + 1):
        sum += i
    print(sum)


def sum_n_cubes(n):
    n = eval(input("Enter a number: "))
    sum = 0
    for i in range(1, n + 1):
        sum += i ** 3
    print(sum)


def encode_better():
    message = input("Enter a message: ")
    cipher = input("Enter a cipher: ")
    encryption = ""
    for c in message:
        encryption = encryption + chr(ord(c) - 97)
    print(encryption)
