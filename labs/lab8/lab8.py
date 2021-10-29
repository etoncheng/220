"""
Name: Eton Cheng
lab8.py

Problem: Functions Practice

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


def number_words():
    in_file_name = input("")
    out_file_name = input("")

    in_file = open(in_file_name, "r")
    out_file = open(out_file_name, "w")

    word_count = ['1', '2', '3', '4', '5', '6', '7']
    sentence = ['The', 'time', 'has', 'come', 'the', 'walrus', 'said']

    for each_list in word_count, sentence:
        list1 = word_count[-1]
        list2 = each_list[-1]
        print(list1, file = out_file)
        print(list2, file = out_file)

    in_file.close()
    out_file.close()


def hourly_wages():
    in_file_name = input("")
    out_file_name = input("")

    in_file = open(in_file_name, "r")
    out_file = open(out_file_name, "w")

    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    hours_worked = eval(input("Enter the number of hours worked: "))
    hourly_wage = 1.65
    pay = hours_worked * hourly_wage
    print("Pay:", first_name, last_name, pay)

    in_file.close()
    out_file.close()


def calc_check_sum():
    ISBN = input("Enter 10-digit number: ")

    while len(ISBN):
        print("10-digits has not been entered, please try again")
    else:
        d1 = int(ISBN[1]) * 10
        d2 = int(ISBN[2]) * 9
        d3 = int(ISBN[3]) * 8
        d4 = int(ISBN[4]) * 7
        d5 = int(ISBN[5]) * 6
        d6 = int(ISBN[6]) * 5
        d7 = int(ISBN[7]) * 4
        d8 = int(ISBN[8]) * 3
        d9 = int(ISBN[9]) * 2
        d10 = int(ISBN[10]) * 1
        sum = (d1+d2+d3+d4+d5+d6+d7+d8+d9+d10)
        ISBN = str(sum)
        print("Your ISBN Number is", ISBN)


def send_message():
    file = open("Bob.txt", "w")
    file.write = ("My friend's name is Bob")
    file.close()


def send_safe_message():
    file = open("Bob.txt", "w")
    file.write = ("My friend's name is Bob")
    file.write.encode("")
    file.close()


def send_uncrackable_message():
    file = open("Bob.txt", "w")
    file.write = ("My friend's name is Bob")
    file.write.encode("")
    file.close()
