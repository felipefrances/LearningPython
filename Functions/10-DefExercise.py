# Jogo de Craps.
# Faça um programa de implemente um jogo de Craps.
# O jogador lança um par de dados, obtendo um valor entre 2 e 12.
# Se, na primeira jogada, você tirar 7 ou 11, você tem um "natural" e ganhou.
# Se você tirar 2, 3 ou 12 na primeira jogada, isto é chamado de "craps" e você perdeu.
# Se, na primeira jogada, você fez um 4, 5, 6, 8, 9 ou 10,este é seu "Ponto".
# Seu objetivo agora é continuar jogando os dados até tirar este número novamente.
# Você perde, no entanto, se tirar um 7 antes de tirar este Ponto novamente.

import random


controle = 1


while controle == 1:
    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)

    resultado = dado1 + dado2

    print(f"Dado 1: {dado1}")
    print(f"Dado 2: {dado2}")
    print(f"Resultado: {resultado}")

    if resultado == 7 or resultado == 11:
        print("Você tem um natural. Parabéns você ganhou no CRAPS!")
        break

    elif resultado == 2 or resultado == 3 or resultado == 12:
        print("CRAPS! Você perdeu...")
        break

    else:
        # while resultado != 7:
        #     print("Você fez um ponto. Jogue novamente: ")

        if resultado == 7:
            print("CRAPS! Você perdeu...")
            break


        if resultado == 7:
            print("CRAPS! Você perdeu...")
            break

# FALTANDO O FINAL DO CÓDIGO.

