"""John Fisherman, a good man, bought a PC to control his work´s daily income.
Every time he brings more fish than that established by the fishing regulations(50 kilograms),
he must pay a fine of $ 4.00 per excess kilogram.
John needs you to write a program that reads the fish weight and calculates the excess.
Record the kilograms beyond the limit and calculate the fine that John will have to pay.
Print the program data with the appropriate messages."""

fish = float(input("Hi John, how much kilograms of fish did you fished today? Please enter the weight: "))

exceed = (fish - 50)
fine = exceed * 4

print("For your today's fishing, you exceed", exceed, "kilograms above established. You have to pay a fine of $", fine)
