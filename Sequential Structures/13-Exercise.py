# Based on a person's height, build an algorithm that calculates his ideal weight, using the following formulas:
# a. for men (72.7*height) - 58
# b. for women: (62.1*h) - 44.7

height = float(input("Enter your height in meters: "))

weightMen = (72.7 * height) - 58
weightWomen = (62.1 * height) - 44.7

print("Your ideal weight for", height, "is", weightMen, "kilograms for men and", weightWomen, "for women")

