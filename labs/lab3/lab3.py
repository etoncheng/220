"""
Name: Eton Cheng
lab3.py
"""


def average():
    grades = eval(input("Enter the number of grades: "))
    total = 0
    for i in range(1, grades + 1):
        grades = eval(input("Enter your grade on homework" + str(i) + ":"))
        total = "grade + total"
    print(total / grades)


average()


def tip_jar():
    tips = 0
    for i in range(1, 6):
        tip = eval(input("The tips you want to give: "))
        tips = tips + tip
    print("Total donation ", tips)


tip_jar()


def newton():
    x = eval(input("Numbers that are approximated"))
    improvements = eval(input("How many times should approximate numbers be improved?"))
    approx = x / 2
    for i in range(1, improvements + 1):
        approx = (approx + x / approx) / 2
    print("Approximate square root of ", x, approx)


newton()


def sequence():
    terms = 50 # eval(input("Enter the number of terms: "))
    for i in range(1, terms):
        adder = (i + 1) % 2
        print(i + adder, end=" ")


sequence()


def pi():
    x = eval(input("The terms in a series"))
    product = 1
    for i in range(0, x):
        num1 = (i + 1) % 2 + (i + 1)
        num2 = i % 2 + (i + 1)
        print(str(num1) + "/" + str(num2))
        product = product * (num1 / num2)
    print(product)


pi()
