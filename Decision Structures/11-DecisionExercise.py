"""The Tabajara Organizations have decided to grant a salary increase to their employees
and have hired you to develop the program that will calculate these adjustments.

Create a program that receives an employee's salary and the adjustment based on the following criteria,
according to the current salary:
- Salaries up to R$ 280.00 (including): 20% increase
- Salaries between R$ 280.00 and R$ 700.00: 15% increase
- Salaries between R$ 700.00 and R$ 1500.00: 10% increase
- Salaries of R$ 1500.00 and above: 5% increase

After the adjustment is made, display on the screen:
- The salary before the adjustment
- The percentage of increase applied
- The amount of the increase
- The new salary after the increase."""

salary = float(input("Enter the employee's salary: "))

if salary <= 280.00:
    percent = 20

elif salary <= 700.00:
    percent = 15

elif salary <= 1500.00:
    percent = 10

else:
    percent = 5

increase = (percent / 100) * salary
newSalary = salary + increase

print(f"The employee´s salary before was $ {salary};")
print(f"Percentage increase applied {percent}%;")
print(f"Amount increased $ {increase};")
print(f"New employee's salary is $ {newSalary}.")
