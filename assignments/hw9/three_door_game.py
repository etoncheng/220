"""
Name: Eton Cheng
three_door_game.py

Problem: choose my favorite door

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""
from graphics import *

win = GraphWin("Three-Door-Game", 600, 600)
win.setCoords(0, 0, 10, 10)

top_text = Text(Point(5, 8), "I have a secret door")
top_text.draw(win)
bottom_text = Text(Point(5, 1), "Click to choose my door")
bottom_text.draw(win)

door1_text = Text(Point(2, 5), "Door1")
door1 = Rectangle(Point(1, 4), Point(3, 6))
door1_text.draw(win)
door1.draw(win)

door2_text = Text(Point(5, 5), "Door2")
door2 = Rectangle(Point(4, 4), Point(6, 6))
door2_text.draw(win)
door2.draw(win)

door3_text = Text(Point(8, 5), "Door3")
door3 = Rectangle(Point(7, 4), Point(9, 6))
door3_text.draw(win)
door3.draw(win)

while True:
    is_clicked = win.getMouse()

    if (is_clicked.getX() > door1.p1.x and is_clicked.getX() < door1.p2.x) \
            and (is_clicked.getY() > door1.p1.y and is_clicked.getY() < door1.p2.y):
        door1.setFill("red")
        door1_text = Text(Point(2, 5), "Door1")
        door1_text.draw(win)
        door1 = Rectangle(Point(1, 4), Point(3, 6))
        door1.draw(win)
        top_text.setText("You Lost!")
        bottom_text.setText("Door3 is my secret door")

    if (is_clicked.getX() > door2.p1.x and is_clicked.getX() < door2.p2.x) \
            and (is_clicked.getY() > door2.p1.y and is_clicked.getY() < door2.p2.y):
        door2.setFill("red")
        door2_text = Text(Point(5, 5), "Door2")
        door2_text.draw(win)
        door2 = Rectangle(Point(4, 4), Point(6, 6))
        door2.draw(win)
        top_text.setText("You Lost!")
        bottom_text.setText("Door3 is my secret door")

    if (is_clicked.getX() > door3.p1.x and is_clicked.getX() < door3.p2.x) \
            and (is_clicked.getY() > door3.p1.y and is_clicked.getY() < door3.p2.y):
        door3.setFill("green")
        door3_text = Text(Point(8, 5), "Door3")
        door3_text.draw(win)
        door3 = Rectangle(Point(7, 4), Point(9, 6))
        door3.draw(win)
        top_text.setText("You Win!")
        bottom_text.setText("Click to close")
