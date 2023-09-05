"""Date in Full Text.
Create a program that prompts the user for their birthdate (dd/mm/yyyy)
and prints the date with the month's name in full text."""

# Import the datetime module to work with dates
import datetime

# Get input from the user
dateInput = input("Please enter your birthdate (dd/mm/yyyy): ")

# Convert the input string to a datetime object
birthdate = datetime.datetime.strptime(dateInput, "%d/%m/%Y")

# Get the full text of the month
month_name = birthdate.strftime("%B")

# Print the date with the month's name in full text
print("Your birthdate is:", birthdate.strftime("%d"), "of", month_name, "of", birthdate.strftime("%Y"))
