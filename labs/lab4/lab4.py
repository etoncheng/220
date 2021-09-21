"""
Name: Eton Cheng
lab4.py

Problem: Graphics and Accumulation Practice

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

from graphics import *
import math


def squares():
    """  <---  You can use tripled quotes to write a multi-line comment....

    Modify the following function to:

    Draw squares (20 X 20) instead of circles. Make sure that the center of the square
    is at the point where the user clicks. Make the window 400 by 400.

    Have each successive click draw an additional square on the screen (rather
    than just moving the existing one).

    Display a message on the window "Click again to quit" after the loop, and
    wait for a final click before closing the window.
    """
    # Creates a graphical window
    width = 400
    height = 400
    win = GraphWin("Lab 4", width, height)

    # number of times user can move square
    num_clicks = 5

    # create a space to instruct user
    inst_pt = Point(width / 2, height - 10)
    instructions = Text(inst_pt, "Click to move square")
    instructions.draw(win)

    # builds a square
    shape = Rectangle(Point(50, 50), Point(20, 20))
    shape.setOutline("red")
    shape.setFill("red")
    shape.draw(win)

    # allows the user to click multiple times to move the square
    for i in range(num_clicks):
        p = win.getMouse()
        c = shape.getCenter()  # center of square

        # move amount is distance from center of square to the
        # point where the user clicked
        dx = p.getX() - c.getX()
        dy = p.getY() - c.getY()
        shape.move(dx, dy)
        shape = Rectangle(Point(50, 50), Point(20, 20))
        shape.setOutline("red")
        shape.setFill("red")
        shape.draw(win)

    win.getMouse()
    win.close()


squares()


def rectangle():
    """
    This program displays information about a rectangle drawn by the user.
    Input: Mouse clicks for the opposite corners of a rectangle.
    Output: Draw the rectangle.
    """
    # Creates a graphical window
    win = GraphWin("Draw a rectangle", 400, 400)

    p1 = win.getMouse()
    p1.draw(win)
    p2 = win.getMouse()
    p2.draw(win)
    p3 = win.getMouse()
    p3.draw(win)
    p4 = win.getMouse()
    p4.draw(win)

    rectangle = Polygon(p1, p2, p3, p4)
    rectangle.setFill("green")
    rectangle.setOutline("blue")
    rectangle.draw(win)

    win.getMouse()
    win.close()


rectangle()


def circle():
    # Creates a graphical window
    win = GraphWin("Draw a rectangle", 400, 400)
    p1 = win.getMouse()
    p1.draw(win)
    p2 = win.getMouse()
    p2.draw(win)

    x1 = p1.getX()
    x2 = p1.getX()
    y1 = p2.getY()
    y2 = p2.getY()

    radius = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

    win.getMouse()
    win.close()

circle()


def pi2():
    pi = 0
    n = 4
    d = 1
    for d in range(1, 12):
        a = 2 * (d % 2) - 1
        pi += a * n / d
        d += 2

    print(pi)


pi2()