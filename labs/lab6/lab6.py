"""
Name: Eton Cheng
lab6.py

Problem: Elementary Strings Practice

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


def name_reverse():
    # Example: Thomas Jefferson
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    print(last_name + ", " + first_name)


name_reverse()


def company_name():
    # Example: www.Amazon.com
    internet_domain_name = input("Enter internet domain name: ")
    company_name_only = internet_domain_name[4:10]
    print(company_name_only)


company_name()


def initials():
    # Example: Travis Stalvey
    student_first_name = input("Enter the first name of student: ")
    student_last_name = input("Enter the last name of student: ")
    first_name_initial = student_first_name[0]
    last_name_initial = student_last_name[0]
    student_initials = first_name_initial + last_name_initial
    print("Tradd's initals are", student_initials)


initials()


def names():
    # Example: Randall Alexander, Tony Leclerc, RoxAnn Stalvey, Walter Blair
    name = input("Enter some names: ")
    name_list = name.split()
    for part in name_list:
        print(part[0].upper() + "", end=" ")
    print()


names()


def thirds():
    sentence = input("Enter a sentence: ")
    sentence_length = len(sentence)
    for i in range(2, sentence_length, 3):
        print(sentence[i], end=" ")


thirds()


def word_average():
    sentence = input("Enter a sentence: ")
    SumAccum = 0
    for ch in sentence.split():
        character = len(ch)
        SumAccum = SumAccum + character
    average = (SumAccum) / (len(sentence.split()))
    print("Average word length:", average)


word_average()


def pig_latin():
    words = str(input("Input Sentence: ")).split()
    for word in words:
        print(word[1:] + word[0] + "ay", end=" ")
    print()


pig_latin()
