#
# CREATE TABLE public.alunos (
# 	nome varchar NULL,
# 	idade varchar NULL,
# 	matricula varchar NULL
# );
#
#
# #################### Exemplo Tkinter 1 #########################
#
from tkinter import *
import psycopg2

#
# def cadastrar():
#     conectar = psycopg2.connect(database="postgres", user="postgres", password="1234", host="localhost")
#     cur = conectar.cursor()
#
#     nome = str(inNome.get()).strip().title()
#     idade = int(inIdade.get())
#     matricula = str(inMatricula.get()).strip().title()
#
#     cur.execute(f"INSERT INTO alunos(nome, idade, matricula) VALUES ('{nome}', {idade}, '{matricula}')")
#
#     conectar.commit()
#     cur.close()
#     conectar.close()
#     confirma()
#
#
# def confirma():
#     novaJanela = Tk()
#     novaJanela.title("Sucesso")
#     novaJanela.geometry("200x80")
#     Label(novaJanela, text="Cadastro feito com Sucesso").place(x=10, y =10,)
#     novo = Button(novaJanela, text="OK", command=lambda: novaJanela.destroy())
#     novo.place(x=80, y=30)
#
#
# def limpar():
#     inNome.delete(0, END)
#     inIdade.delete(0, END)
#     inMatricula.delete(0, END)
#
#
# janela = Tk()
# janela.title("Formulário de Cadastro")
# janela.geometry("500x500")
# #janela.resizable(False, False)
#
# resLabel = StringVar()
# cadastro_frame = Frame(janela)
#
#
# bemvindoLabel = Label(janela, text="Bem Vindo ao Programa Desktop - Python!", font="Arial 15")
#
# #Labels
# nomeLabel = Label(cadastro_frame, text="Nome:", font="Arial 15")
# idadeLabel = Label(cadastro_frame, text="Idade:", font="Arial 15")
# matriculaLabel = Label(cadastro_frame, text="Matricula:", font="Arial 15")
# resultadoLabel = Label(cadastro_frame, textvariable=resLabel)
# botaoCadastro = Button(janela, text="Cadastrar", command=cadastrar, borderwidth=3, height=1, width=10)
# botaoLimpa = Button(janela, text="Limpar", command=limpar, borderwidth=3, height=1, width=10)
#
# bemvindoLabel.grid(padx=70, pady=50)
#
# '''
# nomeLabel.grid(row=3, column=0)
# idadeLabel.grid(row=4, column=0)
# matriculaLabel.grid(row=5, column=0)
# resultadoLabel.grid(row=6, column=0)
# botaoCadastro.place(x=50, y=200)
# botaoLimpa.place(x=150, y=200)
# '''
# #Formatação das Labels
# nomeLabel.grid(row=0, column=0, padx=10, pady=5, sticky='w')
# idadeLabel.grid(row=1, column=0, padx=10, pady=5, sticky='w')
# matriculaLabel.grid(row=2, column=0, padx=10, pady=5, sticky='w')
#
#
# #Entradas de Texto
# inNome = Entry(cadastro_frame)
# inIdade = Entry(cadastro_frame)
# inMatricula = Entry(cadastro_frame)
#
# #Formatação das Entradas de Texto
# inNome.grid(row=0, column=1, padx=10, pady=5)
# inIdade.grid(row=1, column=1, padx=10, pady=5)
# inMatricula.grid(row=2, column=1, padx=10, pady=5)
#
#
# '''
# inNome.grid(row=3, column=1)
# inIdade.grid(row=4, column=1)
# inMatricula.grid(row=5, column=1)
# '''
#
# #Formatação dos Botões - usando place
# resultadoLabel.grid(row=3, column=0, padx=10, pady=5, sticky='w')
# botaoCadastro.place(x=20, y=250)
# botaoLimpa.place(x=150, y=250)
#
#
# cadastro_frame.place(y=100)
# janela.mainloop()
#
#
#
##
#
# #https://www.javatpoint.com/python-tkinter-listbox
#
#
# ################ Exemplo Tkinter 2 #############################
#
#
#
#
# _fundo, fg=cor_label, font=("Helvetica", 12)).grid(row=0, column=0, padx=10, pady=5, sticky='w')
# Label(root, text="Idade:", bg=cor_de_fundo, fg=cor_label, font=("Helvetica", 12)).grid(row=1, column=0, padx=10, pady=5, sticky='w')
# Label(root, text="Matrícula:", bg=cor_de_fundo, fg=cor_label, font=("Helvetica", 12)).grid(row=2, column=0, padx=10, pady=5, sticky='w')
#
# # Entradas de Texto
# nome_entry = Entry(root, font=("Helvetica", 12))
# nome_entry.grid(row=0, column=1, padx=10, pady=5)import tkinter as tk
# from tkinter import Entry, Label, Button
#
# def salvar_dados():
#     # Aqui você pode adicionar lógica para salvar os dados
#     print("Dados salvos")
#
# def limpar_campos():
#     # Aqui você pode adicionar lógica para limpar os campos de entrada
#     nome_entry.delete(0, 'end')
#     idade_entry.delete(0, 'end')
#     matricula_entry.delete(0, 'end')
#
# # Criar janela principal
# root = tk.Tk()
# root.title("Aula de Algoritmos - Python Desktop!")
#
# # Definir esquema de cores
# cor_de_fundo = "#f2f2f2"# This is a sample Python script.
#
# # Press Shift+F10 to execute it or replace it with your code.
# # Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
#
#
# def print_hi(name):# This is a sample Python script.
#
# # Press Shift+F10 to execute it or replace it with your code.
# # Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
#
#
# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
#
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')
#
# # See PyCharm help at https://www.jetbrains.com/help/pycharm/
#
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
#
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')
#
# # See PyCharm help at https://www.jetbrains.com/help/pycharm/
#
# cor_label = "#333333"
# cor_botoes = "#4CAF50"
#
# root.configure(bg=cor_de_fundo)
#
# # Labels
# Label(root, text="Nome do Aluno:", bg=cor_de
# idade_entry = Entry(root, font=("Helvetica", 12))
# idade_entry.grid(row=1, column=1, padx=10, pady=5)
# matricula_entry = Entry(root, font=("Helvetica", 12))
# matricula_entry.grid(row=2, column=1, padx=10, pady=5)
#
# # Botão de Salvar
# Button(root, text="Salvar", command=salvar_dados, bg=cor_botoes, fg="white", font=("Helvetica", 12)).grid(row=3, column=0, pady=10, padx=10, columnspan=2, sticky='ew')
#
# # Botão de Limpar
# Button(root, text="Limpar", command=limpar_campos, bg=cor_botoes, fg="white", font=("Helvetica", 12)).grid(row=4, column=0, pady=10, padx=10, columnspan=2, sticky='ew')
#
# # Adicionar imagem de exemplo para a logo do Programa
# # logo_img = tk.PhotoImage(file='exemplo_logo.png')
# # logo_label = tk.Label(root, image=logo_img, bg=cor_de_fundo)
# # logo_label.grid(row=5, columnspan=2, pady=10)
#
# # Loop principal
# root.mainloop()
