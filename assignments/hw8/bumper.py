"""
Name: Eton Cheng
bumper.py

Problem: 2 bumper cars altering directions upon collisions

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""
from graphics import *

win = GraphWin("Bumper Cars", 600, 600)

pointA = Point(300, 300)
pointB = Point(200, 200)
radius = 30

circleA = Circle(pointA, radius)
circleA.setFill("red")
circleA.setOutline("red")
circleB = Circle(pointB, radius)
circleB.setFill("blue")
circleB.setOutline("blue")

circleA.draw(win)
circleB.draw(win)

dx = 1
dy = 1

xFloor = radius
xCeiling = win.getWidth() - radius
yFloor = radius
yCeiling = win.getHeight() - radius

while True:
    time.sleep(0.01)
    circleA.move(dx, dy)
    if circleB.getCenter().getX() <= xFloor or circleA.getCenter().getX() >= xCeiling:
        dx = -dx
    elif circleA.getCenter().getY() <= yFloor or circleA.getCenter().getY() >= yCeiling:
        dy = -dy
    circleB.move(dx, dy)
    if circleB.getCenter().getX() <= xFloor or circleB.getCenter().getX() >= xCeiling:
        dx = -dx
    elif circleB.getCenter().getY() <= yFloor or circleB.getCenter().getY() >= yCeiling:
        dy = -dy
