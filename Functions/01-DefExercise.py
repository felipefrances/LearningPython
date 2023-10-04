# Faça um programa para imprimir:
#     1
#     2   2
#     3   3   3
#     .....
#     n   n   n   n   n   n  ... n
# para um n informado pelo usuário. Use uma função que receba um valor n inteiro e imprima até a n-ésima linha.


def pyramid(num):
    for i in range(1, num + 1):
        line = ""
        for j in range(i):
            line += str(i) + " "
        print(line.strip())


n = int(input("Enter a number(n): "))

pyramid(n)
