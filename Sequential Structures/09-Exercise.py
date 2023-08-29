# Make a Program that asks for the temperature in Fahrenheit, transforms it and shows the temperature in Celsius.


# Get input from the user for Fahrenheit degrees:
fahrenheit = float(input("Enter the temperature in Fahrenheit degrees: "))

# Transform it in Celsius degrees ( C = 5 * ((F-32) / 9))
celsius = 5 * (fahrenheit - 32) / 9

# Display the calculated value
print(fahrenheit, "degrees equals ", celsius, "degrees in Celsius")
