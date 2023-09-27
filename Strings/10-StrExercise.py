"""Number in Full Text.
Write a program that prompts the user to enter a number from 1 to 99 and prints it in full text on the screen."""

units = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
specials = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
dozens = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
i = 0
j = 0

N = int(input("Enter a number up to 99 "))

if N > 99 or N < 0: print("Invalid number")

if N == 0: print("Zero")

elif N <= 9:
    for i in range(9):
        if N == i + 1: print(units[i])

elif 10 <= N < 20:
    for i in range(9):
        if N == i + 10: print(specials[i])

elif N >= 20:
    if N == 20: print(dozens[0])

    for i in range(9):
        if N == i + 21:
            print(dozens[0] + "-" + units[i])

    if N == 30: print(dozens[1])

    for i in range(9):
        if N == i + 31:
            print(dozens[1] + "-" + units[i])

    if N == 40: print(dozens[2])

    for i in range(9):
        if N == i + 41:
            print(dozens[2] + "-" + units[i])

    if N == 50: print(dozens[3])

    for i in range(9):
        if N == i + 51:
            print(dozens[3] + "-" + units[i])

    if N == 60: print(dozens[4])

    for i in range(9):
        if N == i + 61:
            print(dozens[4] + "-" + units[i])

    if N == 70: print(dozens[5])

    for i in range(9):
        if N == i + 71:
            print(dozens[5] + "-" + units[i])

    if N == 80: print(dozens[6])

    for i in range(9):
        if N == i + 81:
            print(dozens[6] + "-" + units[i])

    if N == 90: print(dozens[7])

    for i in range(9):
        if N == i + 91:
            print(dozens[7] + "-" + units[i])
