"""
Name: Eton Cheng
vigenere.py

Problem: Write a program to implement the Vigenere cipher

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""
from graphics import *

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

letter_to_index = dict(zip(alphabet, range(len(alphabet))))
index_to_letter = dict(zip(range(len(alphabet)), alphabet))


def encrypt(message, key):
    encrypted = ''

    split_message = [message[i:i + len(key)] for i in range(0, len(message), len(key))]

    for each_split in split_message:
        i = 0
        for letter in each_split:
            number = (letter_to_index[letter] + letter_to_index[key[i]]) % len(alphabet)
            encrypted += index_to_letter[number]
            i += 1

    return encrypted


def main():
    win = GraphWin("Vigenere", 500, 500)
    win.setCoords(0, 0, 10, 10)

    plaintext = Text(Point(2, 9), "Message to code")
    plaintext.draw(win)

    user_input1 = Entry(Point(6.5, 9), 30)
    user_input1.draw(win)

    key = Text(Point(2, 8), "Enter Keyword")
    key.draw(win)

    user_input2 = Entry(Point(5, 8), 15)
    user_input2.draw(win)

    button_text = Text(Point(5, 6), "Encode")
    button_outline = Rectangle(Point(6, 7), Point(4, 5))
    button_text.draw(win)
    button_outline.draw(win)

    cipher = Text(Point(5, 4), "Resulting Message")
    cipher.draw(win)

    output_text = Text(Point(5, 3), "")
    output_text.draw(win)

    output_label = Text(Point(5, 1), "Click Anywhere to Close Window")
    output_label.draw(win)

    win.getMouse()

    plaintext = user_input1.getText()

    key = user_input2.getText()

    cipher = encrypt(plaintext, key)

    output_text.setText(cipher)

    win.getMouse()


main()
