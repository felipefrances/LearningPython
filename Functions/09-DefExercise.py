# Reverso do número. Faça uma função que retorne o reverso de um número inteiro informado. Por exemplo: 127 -> 721

def reverso(n):
    n = str(n)
    n = (n[::-1])
    n = int(n)
    print(n)


num = int(input("Digite um numero: "))
reverso(num)

