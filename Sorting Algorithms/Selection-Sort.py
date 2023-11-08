def selectionSort(vetor):
    n = len(vetor)
    for i in range(n):
        indice = i
        for j in range(i + 1, n):
            if vetor[j] < vetor[indice]:
                indice = j
        vetor[i], vetor[indice] = vetor[indice], vetor[i]

# Exemplo de uso:
numeros = [5, 29, 12, 84, 35, 47, 96, 2, 7]
print("Lista não ordenada:", numeros)

selectionSort(numeros)

print("Lista ordenada:", numeros)
    
