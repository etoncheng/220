"""
Name: Eton Cheng
algorithms.py

Problem: algorithms for lab 12

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


def read_data():
    with open('dataSorted.txt', 'r') as file:
        size_to_read = 10
        file_contents = file.read(size_to_read)
        while len(file_contents) > 0:
            print(file_contents, end='')
            file_contents = file.read(size_to_read)


def is_in_linear():
    search_values = eval(input("Type in a value: "))
    values = open('dataStored.txt', 'r')
    if search_values == values:
        return True
    else:
        return False
