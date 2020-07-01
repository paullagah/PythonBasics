class Student:
    group = "student"

    def __init__(self, name, age, group):
        self.name = name
        self.age = age
        self.group = group


def average():
    print(input("What is your name? "))
    test1 = int(input("1st test: "))
    test2 = int(input("2nd test: "))
    test3 = int(input("3rd test: "))

    return (test1 + test2 + test3) / 3


print(average())
