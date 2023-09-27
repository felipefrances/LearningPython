"""
A gas station is selling fuel with the following discount table:
Alcohol:
up to 20 liters, 3% discount per liter
over 20 liters, 5% discount per liter
Gas:
up to 20 liters, 4% discount per liter
over 20 liters, 6% discount per liter
Write an algorithm that reads the number of liters sold, the type of fuel (coded as follows: A-alcohol, G-gasoline),
calculate and print the amount to be paid by the customer knowing that the price of a liter of gasoline is R$ 2.50
the price of a liter of alcohol is R$1.90.
"""

fuel = str(input("Enter A for alcohol or G for gasoline: \n"))
liters = int(input("Enter the number of liters: \n"))

if fuel.upper() == "A":
    value = liters * 1.90
    if liters <= 20:
        fee = value - (value * 0.03)
    else:
        fee = value - (value * 0.05)


elif fuel.upper() == "G":
    value = liters * 2.50
    if liters <= 20:
        fee = value - (value * (4 / 100))
    else:
        fee = value - (value * (6 / 100))

else:
    print("Invalid character.")

print("Fee:", fee)
