"""In a gymnastics competition, each athlete receives scores from seven judges.
The highest and lowest scores are discarded. Your score is then the average of the remaining votes.
You should create a program that takes the gymnast's name and the scores given by the seven judges for their performance
Afterward, it should calculate and report the average score based on the aforementioned procedure
(removing the best and worst scores, then calculating the average with the remaining ones).
The scores are not provided in any particular order."""

nome = input("Digite o nome do atleta: ")
notas = [0, 0, 0, 0, 0, 0, 0]
totalNotas = 0
notaMax = 0
notaMin = 10.1

for i in range(7):
    notas[i] = float(input(f"Digite a {i + 1} nota do atleta: "))
    totalNotas = totalNotas + notas[i]

    if notas[i] < 0 or notas[i] > 10:
        print("Nota inválida. Notas devem ter o valor de 0 a 10.")
        notas[i] = float(input(f"Digite a {i + 1} nota do atleta: "))

    elif notas[i] > notaMax:
        notaMax = notas[i]
    elif notas[i] < notaMin:
        notaMin = notas[i]


media = totalNotas / 7

print(" ")
print('__' * 50)
print(" ")

print(f"Nome do Atleta: {nome}")
for i in range(7):
    print(f"Nota {i+1}: {notas[i]} ")
print(f"""
Resultado final:
Atleta: {nome}
Melhor nota: {notaMax}
Pior nota: {notaMin}
Média: {media}""")