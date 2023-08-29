"""Make a program that asks for 2 integers and a real number. Calculate and show:
a. the product of twice the first and half of the second.
b. the sum of three times the first and the third.
c. the third cubed."""

# Ask for user inputs:
num1 = int(input("Enter the 1st integer number: "))
num2 = int(input("Enter the 2nd integer number: "))
numReal = float(input("Enter a real number: "))

# a. calculate the product of twice the first (2 * num1) and half of the second (num2 /2).
calcA = (num1 * 2) * (num2 / 2)

# b. calculate the sum of three times the first (num1 * 3) and the third (numReal).
calcB = float(num1*3) + numReal

# c. calculate the third cubed (numReal ^3).

calcC = numReal ** 3

# Display the calculated values
print("The product of twice", num1, "and half of", num2, "equals: ", calcA)
print("The sum of three times the", num1, "and", numReal, "equals: ", calcB)
print("The", numReal, "cubed equals", calcC)
