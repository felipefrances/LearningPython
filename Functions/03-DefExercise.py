# Faça um programa, com uma função que necessite de três argumentos,
# e que forneça a soma desses três argumentos.


def funcaoSoma(a, b, c):
    return a + b + c


num1 = int(input("Digite o 1º número: "))
num2 = int(input("Digite o 2º número: "))
num3 = int(input("Digite o 3º número: "))

soma = funcaoSoma(num1, num2, num3)
print(f"Resultado da soma: {soma}")
