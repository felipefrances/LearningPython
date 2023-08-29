# Based on a person's height, build an algorithm that calculates his ideal weight, using the following formula: (72.7*height) - 58

height = float(input("Enter your height in meters: "))

weight = (72.7 * height) - 58

print("Your ideal weight for", height, "is", weight, "kilograms")
