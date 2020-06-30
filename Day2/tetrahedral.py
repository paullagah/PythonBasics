import math

number = float(input("Enter the number of balls: "))    # asks for the volume

def vol(number):
    a = ((math.sqrt(2) * (3 * (number))) ** 0.33)         # a = (square root(2) * (3 * Volume) to the power of 1/3rd
    base = (math.sqrt(3) * (a * a))                         # surface area = square root(3) * (a * a)
    return round(base, 2)

print("Surface area is: ", vol(number))
