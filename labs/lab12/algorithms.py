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


def is_in_linear(search_values, values):
    for i in range(len(values)):
        if values[i] == search_values:
            return i
    return -1


def is_in_binary(search_values, values):
    low = 0
    high = len(values) - 1
    while low <= high:
        mid = (low + high) // 2
        item = values[mid]
        if search_values == item:
            return mid
        elif search_values < item:
            high = mid - 1
        else:
            low = mid + 1
    return -1


def selection_sort(values):
    n = len(values)
    for bottom in range(n-1):
        y = bottom
        for i in range(bottom + 1, n):
            if values[i] < values[y]:
                y = i
        values[bottom], values[y] = values[y], values[bottom]
