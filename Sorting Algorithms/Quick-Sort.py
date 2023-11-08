# eleger um pivô para fazer comparações

def quickSort(lista):
    quickSortHelper(lista, 0, len(lista) - 1)


def quickSortHelper(lista, primeiro, ultimo):
    if primeiro < ultimo:
        pontoDeDivisao = particao(lista, primeiro, ultimo)

        quickSortHelper(lista, primeiro, pontoDeDivisao - 1)
        quickSortHelper(lista, pontoDeDivisao + 1, ultimo)


def particao(lista, primeiro, ultimo):
    pivo = lista[primeiro]

    esquerda = primeiro + 1
    direita = ultimo

    done = False
    while not done:

        while esquerda <= direita and lista[esquerda] <= pivo:
            esquerda = esquerda + 1

        while lista[direita] >= pivo and direita >= esquerda:
            direita = direita - 1

        if direita < esquerda:
            done = True
        else:
            temp = lista[esquerda]
            lista[esquerda] = lista[direita]
            lista[direita] = temp

    temp = lista[primeiro]
    lista[primeiro] = lista[direita]
    lista[direita] = temp

    return direita


lista = [54, 26, 93, 17, 77, 31, 44, 55, 20]
quickSort(lista)
print(lista)
