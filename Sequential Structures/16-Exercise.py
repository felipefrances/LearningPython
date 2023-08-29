# Constants
COVERAGE_PER_LITER = 3  # square meters
CAN_SIZE = 18  # liters
CAN_PRICE = 80.00  # R$

# Input: Size of the area to be painted in square meters
area_to_paint = float(input("Enter the size of the area to be painted in square meters: "))

# Calculate the required amount of paint in liters
required_paint_liters = area_to_paint / COVERAGE_PER_LITER

# Calculate the number of paint cans needed (rounding up)
num_cans_needed = int(required_paint_liters / CAN_SIZE)
if required_paint_liters % CAN_SIZE != 0:
    num_cans_needed += 1

# Calculate the total price
total_price = num_cans_needed * CAN_PRICE

# Display the results
print(f"You'll need {num_cans_needed} cans of paint.")
print(f"The total price is: R$ {total_price:.2f}")
