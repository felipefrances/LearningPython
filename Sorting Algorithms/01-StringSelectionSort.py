def selectionSort(lista):
    n = len(lista)
    for i in range(n):
        indice = i
        for j in range(i+1, n):
            if lista[j].lower() < lista[indice].lower():
                indice = j
        lista[i], lista[indice] = lista[indice], lista[i]

# Exemplo de uso:
animais = ['cachorro', 'gato', 'Macaco', 'papagaio', 'Elefante', 'urso']
selectionSort(animais)
print(animais)
