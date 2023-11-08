# Fazer a soma recursiva de números da lista

def somaRecursiva(lista):
    if not lista:
        return 0
    else:
        return lista[0] + somaRecursiva(lista[1:])


lista = [1, 2, 3, 4, 5]
soma = somaRecursiva(lista)
print(soma)
