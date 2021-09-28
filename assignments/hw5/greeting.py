"""
Name: Eton Cheng
greeting.py

Problem: drawing a heart for greeting card

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""
from graphics import *


def main():
    win = GraphWin("Valentine's Day", 500, 500)
    win.setCoords(0, 0, 10, 10)

    # Draw a heart saying "Happy Valentine's Day!"
    card_shape1 = Circle(Point(3.5, 7), 1.6)
    card_shape1.setFill("red")
    card_shape1.setOutline("red")
    card_shape1.draw(win)

    card_shape2 = Circle(Point(6.4, 7), 1.6)
    card_shape2.setFill("red")
    card_shape2.setOutline("red")
    card_shape2.draw(win)

    card_shape3 = Polygon(Point(2, 7), Point(5, 1), Point(8, 7))
    card_shape3.setFill("red")
    card_shape3.setOutline("red")
    card_shape3.draw(win)

    card_text = Text(Point(5, 5), "Happy Valentine's Day!")
    card_text.draw(win)

    # Draw an arrow and animate it to shoot the heart
    aLine = Line(Point(1, 1), Point(2, 2))
    aLine.setArrow("last")
    aLine.draw(win)

    for i in range(1, 100):
        aLine.move(1, 1)
        time.sleep(0.4)

    message = Text(Point(5, 0.5), "Click anywhere to close")
    message.draw(win)
    win.getMouse()
    win.close()


if __name__ == '__main__':
    main()
