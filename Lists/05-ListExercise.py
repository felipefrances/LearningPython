# Faça um Programa que leia 20 números inteiros e armazene-os num vetor.
# Armazene os números pares no vetor PAR e os números IMPARES no vetor impar. Imprima os três vetores.

myList = []
par = []
impar = []

for i in range(20):
    numero = int(input("Enter a number:"))
    myList.append(numero)

    if numero % 2 == 0:
        par.append(numero)
    else:
        impar.append(numero)


print(myList)
print(par)
print(impar)
