"""
Name: Eton Cheng
three_door_game.py

Problem: choose my favorite door

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""
from graphics import *


def main():
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

    win.getMouse()


main()
