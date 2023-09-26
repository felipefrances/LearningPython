# Knowing that str() converts numerical values into strings, calculate how many digits are there in 2 raised to 1 million.

x = 2 ** 1000000
x = str(x)

print(len(x))
