"""
nome = input("Digite o nome do ginasta: ")
listNotas = [int(input(f"Digite a nota {i+1}: ")) for i in range(7)]
newList = [x for x in listNotas if x != max(listNotas) and x != min(listNotas)]

print(f"Resultado final:\n Atleta: {nome}\n Melhor nota: {max(listNotas)}\n Pior nota: {min(listNotas)}\n Média: {float(sum(newList)//5)}")


//código 2

atleta = input("Informe o nome do atleta: ")
notas = []

for x in range(7):
    nota = float(input("Digite uma nota: "))
    notas.append(nota)

notas.sort()
notas.pop(0)
notas.pop(-1)

media = sum(notas)/7
print(media)

// código 3

nome = input("Atleta: ")
notas= [float(input("Nota: ")) for x in range(7)]
'''
notasTratadas = [x for x in notas if x != min(notas) and x != max(notas)]
print(notasTratadas)
'''
maior = float("-inf")
menor = float("inf")
for x in range(0,7):
    if notas[x] > maior:
        maior = notas[x]
    if notas[x] < menor:
        menor = notas[x]
print(f'Resultado Final:\n Atleta: {nome} \n Melhor nota:{maior}\n Pior nota:{menor}\n Media:{(float(sum(notas))-(maior + menor))/ (len(notas)-2)}')

"""


