# Print the even and odd numbers from the matrix.

matriz = [[5, 10, 20, 30], [2, 4, 6, 8], [10, 25, 50, 2], [60, 75, 80, 4]]

# print("Exemplo de matriz de ordem 3x3:\n")
# print(matriz)
# print('--'*50)
# print ("linha 0, coluna 0:", matriz[0][0])
# print ("linha 0, coluna 1:", matriz[0][1])
# print ("linha 0, coluna 2:", matriz[0][2])
# print ("linha 1, coluna 0:", matriz[1][0])
# print ("linha 1, coluna 1:", matriz[1][1])
# print ("linha 1, coluna 2:", matriz[1][2])
# print ("linha 2, coluna 0:", matriz[2][0])
# print ("linha 2, coluna 1:", matriz[2][1])
# print ("linha 2, coluna 2:", matriz[2][2])


# for i in range(0,3):
#     for j in range(0,3):
#         print("Linha ", i, "Coluna ", j, " = ", matriz[i][j])

# for linha in range(0,3):
#     for coluna in range(0,3):
#             print(f'[{matriz[linha][coluna]:^5}]', end='')


for linha in matriz:
    for elemento in linha:
        if elemento % 2 == 0:  # Verifica se o elemento é par
            print([elemento], end=' ')
            # print()  # Imprime uma nova linha após cada linha da matriz

    # print()

print('\n')
print('*************************************************************************************************')

for i in range(0, 3):
    for j in range(0, 3):
        if matriz[i][j] % 2 == 0:
            print("Linha ", i, "Coluna ", j, " = ", matriz[i][j])
