# Module 2
# Exercise 1

number1 = input("Enter whole number: ")
number2 = input("Enter decimal number: ")

integer_number = int(number1)
float_number = float(number2)
round_number = int(round(float_number))

print(number1)
print(number2)
print(round_number)

# Exercise 2

name = "Pep Guardogiola"
age = 3
bark = True
tweet = False

print("My pet is called", name, ", He is", age, "years old.")
print("Statement:", name, "barks.", bark)
print("Statement:", name, "tweets.", tweet)

# Exercise 3

number1 = float(input("Enter First Number: "))
number2 = float(input("Enter Second Number: "))

if number1 > number2:
    number1bigger = True
else:
    number1bigger = False

print("number1bigger:", number1bigger)