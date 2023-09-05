"""Vertical Name in Staircase.
Create a program that asks the user for their name and prints it in a staircase format."""

name = str(input("Enter your name: "))

# Print the name in a staircase format
for i in range(len(name)):
    print(name[:i+1])
