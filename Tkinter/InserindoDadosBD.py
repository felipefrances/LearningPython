from tkinter import *
import psycopg2


def cadastrar():
    conectar = psycopg2.connect(database="postgres", user="postgres", password="1234", host="localhost")
    cur = conectar.cursor()

    nome = str(inNome.get()).strip().title()
    idade = int(inIdade.get())
    matricula = str(inMatricula.get()).strip().title()

    cur.execute(f"INSERT INTO teste(nome, idade, matricula) VALUES ('{nome}', {idade}, '{matricula}')")

    conectar.commit()
    cur.close()
    conectar.close()
    confirmar()

def limpar():
    inNome.delete(0, END)
    inIdade.delete(0, END)
    inMatricula.delete(0, END)


def confirmar():
    janela2 = Tk()
    janela2.title(" ")
    janela2.geometry("200x80")

    texto = Label(janela2, text='Cadastro Realizado')
    botaoOK = Button(janela2, text='OK', command=lambda: janela2.destroy())

    texto.grid(column=0, row=0, pady=10, padx=10, sticky='n')
    botaoOK.grid(column=0, row=1, pady=10, padx=10)

    janela2.mainloop()


# Criando e dando título à janela
janela = Tk()
janela.title('Inserindo dados no Banco de Dados')

# Criando as labels e os botões da janela
nome = Label(janela, text='Nome:', font='Arial 15')
idade = Label(janela, text='Idade:', font='Arial 15')
matricula = Label(janela, text='Matrícula:', font='Arial 15')
botaoCadastro = Button(janela, text='Cadastrar', font='Arial', command=cadastrar, pady=5, padx=5)
botaoLimpar = Button(janela, text='  Limpar ', font='Arial', command=limpar, pady=5, padx=5)

# Posicionando as labels e os botões na janela
nome.grid(column=0, row=0, pady=10, padx=10)
idade.grid(column=0, row=1, pady=10, padx=10)
matricula.grid(column=0, row=2, pady=10, padx=10)
botaoCadastro.grid(column=0, row=4, pady=10, padx=10)
botaoLimpar.grid(column=1, row=4, pady=10, padx=10)

# Criando as entradas de dados
inNome = Entry(janela)
inIdade = Entry(janela)
inMatricula = Entry(janela)

# Posicionando as entradas de dados
inNome.grid(column=1, row=0, pady=10, padx=10)
inIdade.grid(column=1, row=1, pady=10, padx=10)
inMatricula.grid(column=1, row=2, pady=10, padx=10)

janela.mainloop()
