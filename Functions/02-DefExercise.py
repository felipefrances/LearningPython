# Faça um programa para imprimir:
#     1
#     1   2
#     1   2   3
#     .....
#     1   2   3   ...  n

def pyramid2(n):
    for i in range(1, n + 1):
        line = ""
        for j in range(1, i + 1):
            line += str(j)

    print(line)


num = int(input("Enter a number:"))

pyramid2(num)

