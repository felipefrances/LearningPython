# Crie uma janela que solicite a entrada de dois números e exiba a soma após o clique no botão enviar
# AQUI NÃO ESTÁ SENDO USADO BANCO DE DADOS!!

from tkinter import *

# Criando a função somar do botão:

def somar():
    num1 = int(campo1.get())
    num2 = int(campo2.get())
    soma = (num1 + num2)

    novaJanela = Tk()
    novaJanela.title("Resultado")
    texto = Label(novaJanela, text=f"Resultado da Soma: {soma}", font='Arial 15')
    texto.grid(column=0, row=0, pady=10, padx=10)

    novo = Button(novaJanela, text="OK", command=lambda: novaJanela.destroy())
    novo.grid(column=0, row=1, pady=10)



# Criando a janela
janela = Tk()
janela.title('Somando dois números')

# Criando as labels da janela
textoInicial = Label(janela, text='Verifique a soma de dois números.', font='Arial 20')
numero1 = Label(janela, text='1º Número: ', font='Arial 15')
numero2 = Label(janela, text='2º Numero: ', font='Arial 15')
botao = Button(janela, text='Somar', font='Arial 15', command=somar)

# posicionando as labels na janela:
textoInicial.grid(column=0, row=0, pady=10, padx=10, sticky='n')
numero1.grid(column=0, row=1, pady=10, padx=10, sticky='w')
numero2.grid(column=0, row=2, pady=10, padx=10, sticky='w')
botao.grid(column=0, row=4, pady=10, padx=100, sticky='s')

# Entradas de texto:
campo1 = Entry(janela)
campo2 = Entry(janela)

#Posicionando as entradas de texto:
campo1.grid(column=0, row=1, pady=10, padx=10)
campo2.grid(column=0, row=2, pady=10, padx=10)

janela.mainloop()