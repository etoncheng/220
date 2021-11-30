"""
Name: Eton Cheng
lab13.py

Problem: Lists Searching

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


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


def star_find(filename):
    with open('signals.txt', 'r') as filename:
        size_to_read = 10
        filename_contents = filename.read(size_to_read)
        while len(filename_contents) > 0:
            print(filename_contents, end='')
            filename_contents = filename.read(size_to_read)
        for i in range(filename):
            if i == 4000 or 5000:
                print("You found a new neutron star!")
            else:
                print("Keep looking!")
