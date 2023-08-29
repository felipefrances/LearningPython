# Make a program that asks for the temperature in degrees Celsius, transforms it and shows it in degrees Fahrenheit.


# Get input from the user for Fahrenheit degrees:
celsius = float(input("Enter the temperature in Celsius degrees: "))

# Transform it in Fahrenheit degrees ( C = 5 * ((F-32) / 9))
fahrenheit = (celsius * 9 / 5) + 32

# Display the calculated value
print(celsius, "degrees equals ", fahrenheit, "degrees in Fahrenheit")
