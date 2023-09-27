# Faça um Programa que leia um vetor de 5 números inteiros e mostre-os.

mylist = []

for i in range(5):
    number = int(input(f"Digite o {i+1}º número inteiro: "))
    mylist.append(number)

# Exiba os números do vetor
print("Numbers entered:")
for num in mylist:
    print(num)
