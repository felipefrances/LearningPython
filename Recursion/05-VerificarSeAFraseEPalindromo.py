def ePalindromo(frase):
    def limparString(frase):
        caracteresValidos = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        fraseLimpa = ""
        for letra in frase:
            if letra in caracteresValidos:
                fraseLimpa += letra
        return fraseLimpa

    def verificarPalindromo(frase):
        if len(frase) <= 1:
            return True
        elif frase[0] != frase[-1]:
            return False
        else:
            return verificarPalindromo(frase[1:-1])

    fraseLimpa = limparString(frase)
    resultado = verificarPalindromo(fraseLimpa)

    return resultado, fraseLimpa[::-1]

# Recebe uma frase do usuário
frase = input("Digite uma frase para verificar se é um palíndromo: ")

# Verifica se é um palíndromo e retorna a frase invertida
resultado, fraseInvertida = ePalindromo(frase)

# Imprime o resultado e a frase invertida
if resultado:
    print(f"A frase '{frase}' é um palíndromo.")
else:
    print(f"A frase '{frase}' não é um palíndromo.")
print(f"Frase invertida: {fraseInvertida}")
