def insertionSort(lista):
    for i in range(1, len(lista)):
        valorAtual = lista[i]
        j = i - 1
        while j >= 0 and valorAtual.lower() < lista[j].lower():
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = valorAtual

# Exemplo de uso:
animais = ['cachorro', 'gato', 'Macaco', 'papagaio', 'Elefante', 'urso']
insertionSort(animais)
print(animais)
