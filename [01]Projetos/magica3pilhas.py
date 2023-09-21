import random

# Definir as dimensões da matriz
linhas = 3
colunas = 7

# Inicializar a matriz com zeros
matriz = [[0 for _ in range(colunas)] for _ in range(linhas)]

# Gerar uma lista de 21 valores aleatórios
valores = random.sample(range(1, 100), 21)

# Distribuir os valores na matriz
indice = 0
for i in range(linhas):
    for j in range(colunas):
        if indice < len(valores):
            matriz[i][j] = valores[indice]
            indice += 1

# Imprimir a matriz
for linha in matriz:
    print(linha)

fileira = int(input("Escolha um número e informe em qual linha ele se encontra:"))

while True:
    fileira = int(input("Escolha um número e informe em qual linha ele se encontra:"))

    if 1 <= fileira <= 3:
        print(fileira)
        break  # Se o input for válido, sai do loop
    else:
        print("Opção inválida.\n")

# if fileira <= 0 or fileira >= 4:
#     print("Opção inválida.\n")
# elif fileira == 1:
#     print(fileira)
# elif fileira == 2:
#     print(fileira)
# elif fileira == 3:
#     print(fileira)