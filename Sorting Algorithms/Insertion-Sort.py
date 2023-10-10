lista = [5, 29, 12, 84, 35, 47, 96, 2, 7]

for i in range(len(lista)):
    valor = lista[i]

    while lista[i] < lista[i - 1] and i > 0:
        lista[i] = lista[i - 1]
        i = i - 1

        lista[i] = valor


    else:
        continue

print(lista)

