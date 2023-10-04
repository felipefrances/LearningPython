# Faça um programa que use a função valorPagamento para determinar o valor a ser pago por uma prestação de uma conta.
# O programa deverá solicitar ao usuário o valor da prestação e o número de dias em atraso
# e passar estes valores para a função valorPagamento, que calculará o valor a ser pago
# e devolverá este valor ao programa que a chamou.
# O programa deverá então exibir o valor a ser pago na tela.
# Após a execução o programa deverá voltar a pedir outro valor de prestação e assim continuar
# até que seja informado um valor igual a zero para a prestação.
# Neste momento o programa deverá ser encerrado, exibindo o relatório do dia,
# que conterá a quantidade e o valor total de prestações pagas no dia.
# O cálculo do valor a ser pago é feito da seguinte forma:
# Para pagamentos sem atraso, cobrar o valor da prestação.
# Quando houver atraso, cobrar 3% de multa, mais 0,1% de juros por dia de atraso.

def valorPagamento(valor, atraso):
    if atraso <= 0:
        return valor
    else:
        return valor + (valor*0.001)*atraso + valor*0.03


prestacao = 1
contador = 0
soma = 0

while prestacao != 0:
    diasAtraso = int(input("Digite os dias de atraso, se houver:"))
    prestacao = float(input("Digite o valor da prestação ou 0 para terminar: "))

    if prestacao == 0:
        break

    elif prestacao > 0:
        contador += 1
        soma += valorPagamento(prestacao, diasAtraso)

print(f"""
Relatório do dia:
Total de prestações pagas: {contador}
Valor total pago: {soma}
""")
