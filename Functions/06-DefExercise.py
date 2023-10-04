# Faça um programa que converta da notação de 24 horas para a notação de 12 horas.
# Por exemplo, o programa deve converter 14:25 em 2:25 P.M.
# A entrada é dada em dois inteiros.
# Deve haver pelo menos duas funções: uma para fazer a conversão e uma para a saída.
# Registre a informação A.M./P.M. como um valor ‘A’ para A.M. e ‘P’ para P.M.
# Assim, a função para efetuar as conversões terá um parâmetro formal para registrar se é A.M. ou P.M.
# Inclua um loop que permita que o usuário repita esse cálculo para novos valores de entrada todas as vezes que desejar.


def conversaoHoras(hora, minuto):
    if hora >= 12:
        hora = hora - 12
        p = "P.M"

    else:
        p = "A.M"

    return hora, minuto, p


def imprimirHorario(hora, min, p):
    print(f"Horário: {hora}:{min} {p}")


continuar = "s"

while continuar == "s":

    hora24 = int(input("Digite a hora (0 a 23): "))
    minutos = int(input("Digite os minutos (00 a 59): "))


    if 0 <= hora24 <= 23 and 0 <= minutos <= 59:
        h, minuto, p = conversaoHoras(hora24, minutos)
        imprimirHorario(h, minuto, p)

    continuar = input("Deseja continuar a inserir horários? (S/N):")

    if continuar.lower() != 's':
        break










