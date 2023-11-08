def moveTower(altura, pinoEsquerda, pinoDireita, pinoMeio):
    if altura >= 1:
        moveTower(altura - 1, pinoEsquerda, pinoMeio, pinoDireita)
        moveDisk(pinoEsquerda, pinoDireita)
        moveTower(altura - 1, pinoMeio, pinoDireita, pinoEsquerda)

def moveDisk(fp,tp):
    print("Movendo o disco de", fp, "para", tp)

moveTower(3,"A","C","B")