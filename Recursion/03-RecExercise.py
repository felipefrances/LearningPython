# Inverter uma string usando recursividade

# SEM RECURSÃO
def inverterStr(s):
    return s[::-1]


# Exemplo de uso
string = input("Digite a palavra ou frase a ser invertida:")
strInvertida = inverterStr(string)
print(strInvertida)


# COM RECURSÃO

def inverterStringRec(s):
    if len(s) <= 1:
        return s
    else:
        return inverterStringRec(s[1:]) + s[0]


# Exemplo de uso
str = input("Digite a palavra ou frase a ser invertida:")
strInvert = inverterStringRec(str)
print(strInvert)
