# Write a program that asks for the radius of a circle, calculates and displays its area.

# library that has pi value

import math

# Get input from the user
radius = float(input("Please enter the radius of the circle: "))

# Calculate the area of the circle (A = π * r^2)
area = math.pi * (radius ** 2)

# Display the area
print("The area of the circle with radius", radius, "is:", area)
