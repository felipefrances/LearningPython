# Faça um programa com uma função chamada somaImposto.
# A função possui dois parâmetros formais: taxaImposto, que é a quantia de imposto sobre vendas expressa
# em porcentagem e custo, que é o custo de um item antes do imposto.
# A função “altera” o valor de custo para incluir o imposto sobre vendas.

def somaImposto(custo, taxa):
    return custo + custo*(taxa/100)


custo = float(input("Digite o custo do produto em reais:"))
imposto = float(input("Digite a % do imposto sobre as vendas:"))

valorFinal = somaImposto(custo, imposto)

print(f"O valor final do produto com o imposto sobre as vendas é de: R$ {valorFinal}")