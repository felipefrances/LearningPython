"""Faça um programa que leia um número indeterminado de valores, correspondentes a notas,
encerrando a entrada de dados quando for informado um valor igual a -1 (que não deve ser armazenado).
Após esta entrada de dados, faça:
Mostre a quantidade de valores que foram lidos;
Exiba todos os valores na ordem em que foram informados, um ao lado do outro;
Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro;
Calcule e mostre a soma dos valores;
Calcule e mostre a média dos valores;
Calcule e mostre a quantidade de valores acima da média calculada;
Calcule e mostre a quantidade de valores abaixo de sete;
Encerre o programa com uma mensagem;
"""

notasLista = []
soma = 0

while True:
    nota = float(input("Digite o valor da nota ou -1 para encerrar: "))
    if nota == -1:
        print("Programa encerrado.")
        break
    else:
        notasLista.append(nota)
        soma += nota

    media = soma / len(notasLista)

    contador = 0

    for i in range(len(notasLista)):
        if notasLista[i] > media:
            contador += 1

    contadorAbaixo = 0

    for i in range(len(notasLista)):
        if notasLista[i] < 7:
            contadorAbaixo += 1

print(f"Total de valores informados: {len(notasLista)}\n")
print(f"Valores informados: {notasLista}\n")
print("Valores informados na ordem inversa:\n")
for i in range(len(notasLista) - 1, -1, -1):
    print(notasLista[i])

print(f"Soma dos valores informados: {soma}")
print(f"Media dos valores informados: {media}")
print(f"Quantidade de valores acima da média de valores: {contador}")
print(f"Quantidade de valores abaixo de 7.0: {contadorAbaixo}")

