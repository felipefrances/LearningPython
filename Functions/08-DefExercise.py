# Faça uma função que informe a quantidade de dígitos de um determinado número inteiro informado.

def digitos(numero):
    numero = str(numero)
    print(f"O número informado tem {len(numero)} dígitos.")


num = int(input("Digite um número inteiro: "))
digitos(num)


