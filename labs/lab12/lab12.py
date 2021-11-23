"""
Name: Eton Cheng
lab12.py

Problem: Loops Lists

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""
import random


def find_and_remove_first():
    list = [1, 2, 3, 4, 5]
    print(list)
    list.remove(1)
    print(list.remove)
    list.pop(0)
    print(list.pop)


def good_input():
    number = int(input("Enter number between 1 and 10: "))
    if 1 <= number <= 10:
        print("Good Input")
    else:
        print("Try Again")


def number_digits():
    number = int(input("Enter a number: "))
    count = 0
    while number > 0:
        count += 1
        number = number // 10
    print(f"Number of digits: {count}")


def high_low_game():
    number = random.randint(1, 100)
    tries = 0

    while True:
        guess = int(input("Guess a number: "))
        tries += 1

        if guess == number and tries <= 7:
            print("Correct!")
            break
        elif guess < number and tries < 7:
            print("Too Low!")
            tries += 1
        elif guess > number and tries < 7:
            print("Too High!")
            tries += 1
        elif tries > 7:
            print("Sorry but you have exceeded the limit of tries.")
