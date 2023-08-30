"""Create a program for a paint store.
The program should prompt the user for the size in square meters of the area to be painted.
Take into consideration that the paint coverage is 1 liter for every 6 square meters
and that the paint is sold in 18-liter cans, which cost $80.00, or in 3.6-liter gallons,
which cost $25.00.

Inform the user about the quantities of paint to be purchased and the corresponding prices
in three situations:

1. Buying only 18-liter cans.
2. Buying only 3.6-liter gallons.
3. Mixing cans and gallons to minimize paint waste.
Add a 10% buffer and always round up the values, meaning consider full cans."""

# Constants
COVERAGE_PER_LITER = 6  # square meters
CAN_SIZE = 18  # liters
CAN_PRICE = 80.00  # $
GALLON_SIZE = 3.6  # liters
GALLON_PRICE = 25.0  # $

# Input: Size of the area to be painted in square meters
area_to_paint = float(input("Enter the size of the area to be painted in square meters: "))

# Calculate the required amount of paint in liters
required_paint_liters = area_to_paint / COVERAGE_PER_LITER

# situation 1 (Buying only 18-liter cans):
# Calculate the number of paint cans needed (10% buffer and rounding up)
num_cans_needed = int(required_paint_liters * 1.1 / CAN_SIZE)
if required_paint_liters % CAN_SIZE != 0:
    num_cans_needed += 1
    print(f"Situation 1: You'll need {num_cans_needed} paint cans")

# situation 2 (Buying only 3.6-liter gallons):
# Calculate the number of paint gallons needed (10% buffer and rounding up)
num_gallons_needed = int(required_paint_liters * 1.1 / GALLON_SIZE)
if required_paint_liters % GALLON_SIZE != 0:
    num_gallons_needed += 1
    print(f"Situation 2: You'll need {num_gallons_needed} paint gallons")

# situation 3 (Mixing cans and gallons to minimize paint waste):
num_can_mixed = int((required_paint_liters * 1.1) / CAN_SIZE)
num_gallons_mixed = int(((required_paint_liters * 1.1) % CAN_SIZE) / GALLON_SIZE)
if ((required_paint_liters * 1.1) % CAN_SIZE) % GALLON_SIZE != 0:
    num_gallons_mixed += 1
    print(f"Situation 3: You'll need {num_can_mixed} paint cans and {num_gallons_mixed} gallons")








