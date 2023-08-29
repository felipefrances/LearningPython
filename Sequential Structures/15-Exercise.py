"""Make a Program that asks how much you earn per hour and the number of hours worked in the month.
Calculate and show your total salary in that month, knowing that 11% is deducted for Income Tax, 8% for INSS and 5% for the Union, make a program that gives us:
a. gross salary.
b. how much did he pay to the INSS.
c. How much did you pay the union?
d. the net salary.
e.calculate the deductions and the net salary, according to the table below:
+ Gross Salary: BRL
- Income tax (11%): BRL
- INSS (8%): BRL
- Union (5%): BRL
= Net Salary: BRL
Note: Gross Salary - Discounts = Net Salary."""

hourSalary = float(input("Please enter your hour-based salary: "))
hourWorked = float(input("Please enter how much hours did you work this month: "))

grossSalary = hourSalary * hourWorked

incomeTax = grossSalary * 11/100
inss = grossSalary * 8/100
unionDiscount = grossSalary * 5/100
netSalary = grossSalary - incomeTax - inss - unionDiscount

print("Here´s your balance sheet:")
print("Gross Salary:", grossSalary, "BRL")
print("Income tax (11%):", incomeTax, "BRL")
print("INSS (8%):", inss, "BRL")
print("Union (5%):", unionDiscount, "BRL")
print("Tour net Salary is", netSalary, "BRL")
