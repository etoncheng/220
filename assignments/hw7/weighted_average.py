"""
Name: Eton Cheng
weighted_average.py

Problem: student average

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


def weighted_average():
    in_file_name = "grades.txt"
    out_file_name = "avg.txt"

    in_file = open(in_file_name, 'r')
    out_file = open(out_file_name, 'w')

    student1 = ["Billy Bother", 20, 89, 30, 94, 50, 82]
    student2 = ["Oh No", 30, 52, 60, 75]
    student3 = ["Hermione Heffalump", 40, 93, 60, 97]
    student4 = ["Too Bad", 90, 95, 10, 87, 20, 94]
    student5 = ["Kurt Kidd", 20, 88, 30, 82, 40, 76, 10, 99]
    print(student1)
    print(student2)
    print(student3)
    print(student4)
    print(student5)

    grades = student1[2::2]
    weights = student1[1::2]

    def average(grades, weights):
        weights_shares = []
        for i in range(0, len(weights)):
            weights_shares.append(weights[i] / sum(weights))

        weights_grades = []
        for i in range(0, len(grades)):
            weights_grades.append(grades[i] * weights_shares[i])

        weighted_average = sum(weights_grades)

        return weighted_average

    print("Billy Bother's average:", average(grades, weights))

    grades = student2[2::2]
    weights = student2[1::2]

    def average(grades, weights):
        weights_shares = []
        for i in range(0, len(weights)):
            weights_shares.append(weights[i] / sum(weights))

        weights_grades = []
        for i in range(0, len(grades)):
            weights_grades.append(grades[i] * weights_shares[i])

        weighted_average = sum(weights_grades)

        return weighted_average

    print("Oh No's average:", average(grades, weights))

    grades = student3[2::2]
    weights = student3[1::2]

    def average(grades, weights):
        weights_shares = []
        for i in range(0, len(weights)):
            weights_shares.append(weights[i] / sum(weights))

        weights_grades = []
        for i in range(0, len(grades)):
            weights_grades.append(grades[i] * weights_shares[i])

        weighted_average = sum(weights_grades)

        return weighted_average

    print("Hermione Heffalump's average:", average(grades, weights))

    grades = student4[2::2]
    weights = student4[1::2]

    def average(grades, weights):
        weights_shares = []
        for i in range(0, len(weights)):
            weights_shares.append(weights[i] / sum(weights))

        weights_grades = []
        for i in range(0, len(grades)):
            weights_grades.append(grades[i] * weights_shares[i])

        weighted_average = sum(weights_grades)

        return weighted_average

    print("Too Bad's average:", average(grades, weights))

    grades = student5[2::2]
    weights = student5[1::2]

    def average(grades, weights):
        weights_shares = []
        for i in range(0, len(weights)):
            weights_shares.append(weights[i] / sum(weights))

        weights_grades = []
        for i in range(0, len(grades)):
            weights_grades.append(grades[i] * weights_shares[i])

        weighted_average = sum(weights_grades)

        return weighted_average

    print("Kurt Kidd's average:", average(grades, weights))

    in_file.close()
    out_file.close()
