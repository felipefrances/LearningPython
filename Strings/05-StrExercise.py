"""Vertical Name.
 Create a program that asks the user for their name and prints it  in an inverted staircase format."""

name = str(input("Enter your name:"))

for i in range(len(name), 0, -1):
    print(name[:i])
