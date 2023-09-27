# Faça um Programa que peça as quatro notas de 10 alunos,
# calcule e armazene num vetor a média de cada aluno,
# imprima o número de alunos com média maior ou igual a 7.0.

alunosAprovados = []
media = 0
mediaLista = []
for i in range(10):
    notasAlunos = []
    for j in range(4):
        nota = float(input(f"Digite a nota {j+1} do aluno {i+1}:"))
        notasAlunos.append(nota)

    soma = 0

    for nota in notasAlunos:
        soma += nota

    media = soma/4
    mediaLista.append(media)

    if media >= 7:
        alunosAprovados.append(media)

print(mediaLista)
print(len(alunosAprovados))





