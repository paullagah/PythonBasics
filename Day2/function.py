student = input("What is your full name? ")
hw = int(input("Homework Grade: "))
assess = int(input("Assessment: "))
fexam = int(input("Final Exam: "))


def grading(hw, assess, fexam):
    return hw + assess + fexam


print(grading(hw, assess, fexam), 'Is your total result')

if grading(hw, assess, fexam) >= (175 * 0.7):
    print("You got an A!")
elif grading(hw, assess, fexam) >= (175 * 0.6):
    print("You got a B!")
elif grading(hw, assess, fexam) >= (175 * 0.5):
    print("You got a C!")
elif grading(hw, assess, fexam) >= (175 * 0.4):
    print("You got a D!")
else:
    print("Failed, try again next year")

