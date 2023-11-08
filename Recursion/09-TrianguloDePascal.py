def calcularBinomio(n, k):
    if k == 0 or k == n:
        return 1
    return calcularBinomio(n - 1, k - 1) + calcularBinomio(n - 1, k)

def gerarLinha(linha):
    return [calcularBinomio(linha, i) for i in range(linha + 1)]

def imprimirTrianguloPascal(numLinhas):
    for linha in range(numLinhas):
        coeficientes = gerarLinha(linha)
        print(' '.join(map(str, coeficientes)).center(numLinhas * 3))

numLinhas = int(input("Digite o número de linhas do Triângulo de Pascal: "))
imprimirTrianguloPascal(numLinhas)
