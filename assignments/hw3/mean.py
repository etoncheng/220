"""
Name: Eton Cheng
mean.py

Problem: Calculating Means

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

# 1. What will the program do?
# It will calculate the rms average, harmonic mean, and geometric mean

# 2. What will be the inputs and outputs?
# The inputs will be the values and formulas and the outputs will be th results

# 3. What is the step-by-step list of what the program must do, aka algorithm?
# Analyze, Specify, Design, Implement, Test, and Maintain

# value a: 10
# value b: 5
# value c: 2
# value d: 5


import math


def rms_average():
    print("This program calculates the root-mean-square average")
    print()
    a = float(input("Enter value a: "))
    b = float(input("Enter value b: "))
    c = float(input("Enter value c: "))
    d = float(input("Enter value d: "))
    numerator = (a * a) + (b * b) + (c * c) + (d * d)
    rms = math.sqrt(numerator / 4)
    print()
    print("The root-mean-square average is: ", round(rms, 3))


rms_average()


def harmonic_mean():
    print("This program calculates the harmonic mean")
    print()
    a = float(input("Enter value a: "))
    b = float(input("Enter value b: "))
    c = float(input("Enter value c: "))
    d = float(input("Enter value d: "))
    numerator = 4
    harmonic = numerator / (1/a + 1/b + 1/c + 1/d)
    print()
    print("The harmonic mean is: ", round(harmonic, 3))


harmonic_mean()


def geometric_mean():
    print("This program calculates the geometric mean")
    print()
    a = float(input("Enter value a: "))
    b = float(input("Enter value b: "))
    c = float(input("Enter value c: "))
    d = float(input("Enter value d: "))
    geometric = (a * b * c * d) ** 0.25
    print()
    print("The geometric mean is: ", round(geometric, 3))


geometric_mean()
