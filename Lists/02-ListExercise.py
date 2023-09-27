# Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.

myList = []

for i in range(10):
    number = float(input(f"Enter the {i + 1}º number: "))
    myList.append(number)

for i in range(len(myList) - 1, -1, -1):
    print(myList[i])

# or you can use reversed():

for num in reversed(myList):
    print(num)
