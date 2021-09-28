"""
Name: Eton Cheng
lab5.py

Problem: Graphics Practice

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


from graphics import *
import math


def triangle():
    win_width = 500
    win_height = 500
    win = GraphWin("Draw a Triangle", win_width, win_height)

    # Add code here to accept mouse clicks, draw the triangle.
    p1 = win.getMouse()
    p1.draw(win)
    p2 = win.getMouse()
    p2.draw(win)
    p3 = win.getMouse()
    p3.draw(win)
    triangle = Polygon(p1, p2, p3)
    triangle.setFill("blue")
    triangle.setOutline("black")
    triangle.draw(win)

    # Display its area in the graphics window.
    x1 = p1.getX()
    x2 = p2.getX()
    x3 = p3.getX()
    y1 = p1.getY()
    y2 = p2.getY()
    y3 = p3.getY()
    dx1 = p1.getX() - p2.getX()
    dx2 = p2.getX() - p3.getX()
    dx3 = p3.getX() - p1.getX()
    dy1 = p1.getY() - p2.getY()
    dy2 = p2.getY() - p3.getY()
    dy3 = p3.getY() - p1.getY()
    a = math.sqrt((dx1 ** 2) + (dy1 ** 2))
    b = math.sqrt((dx2 ** 2) + (dy2 ** 2))
    c = math.sqrt((dx3 ** 2) + (dy3 ** 2))
    perimeter = a + b + c
    s = perimeter / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))

    # Wait for another click to exit
    win.getMouse()
    win.close()


def color_shape():
    '''Create code to allow a user to color a shape by entering rgb amounts'''

    # create window
    win_width = 400
    win_height = 400
    win = GraphWin("Color Shape", win_width, win_height)
    win.setBackground("white")

    # create text instructions
    msg = "Enter color values between 0 - 255\nClick window to color shape"
    inst = Text(Point(win_width / 2, win_height - 20), msg)
    inst.draw(win)

    # create circle in window's center
    shape = Circle(Point(win_width / 2, win_height / 2 - 30), 50)
    shape.draw(win)

    # redTexPt is 50 pixels to the left and forty pixels down from center
    red_text_pt = Point(win_width / 2 - 50, win_height / 2 + 40)
    red_text = Text(red_text_pt, "Red: ")
    red_text.setTextColor("red")

    # green_text_pt is 30 pixels down from red
    green_text_pt = red_text_pt.clone()
    green_text_pt.move(0, 30)
    green_text = Text(green_text_pt, "Green: ")
    green_text.setTextColor("green")

    # blue_text_pt is 60 pixels down from red
    blue_text_pt = red_text_pt.clone()
    blue_text_pt.move(0, 60)
    blue_text = Text(blue_text_pt, "Blue: ")
    blue_text.setTextColor("blue")

    # display rgb text
    red_text.draw(win)
    green_text.draw(win)
    blue_text.draw(win)

    # Wait for another click to exit
    win.getMouse()
    win.close()


def process_string():
    user_input = eval(input("Enter the text: "))
    first = user_input[0]
    print(first)
    last = user_input[-1]
    print(last)
    two_to_five = user_input[2, 6]
    print(two_to_five)
    first_and_last = first + last
    print(first_and_last)
    first_three = user_input[0, 3]
    print(first_three)
    l = len(user_input)
    for i in range(0, 1):
        count = 0
        print(user_input[count])
        count = count + 1
    print(l)


def process_list():
    pt = Point(5, 10)
    values = {5, 'hi', 2.5, 'there', pt, '7.2'}
    x = values[1] + values[3]
    print(x)
    x = values[1] ** 5
    print(x)
    x = values[2], values[3], pt
    print(x)
    x = [values[2], values[3], 5]
    print(x)
    x = [values[2], values[0], values[-1]]
    print(x)
    x = values[2], values[0], values[-1]
    print(x)


def another_series():
    user_input = eval(input("Enter number of terms: ")
    for i in range(0, 1):
        count = 1
        if count == 3:
            sum[i] = 6
            count = 1
        if count == 2:
            sum[i] = 4
            count = 3
        if count == 1:
            sum[i] = 2
            count = 2
        print(sum)
