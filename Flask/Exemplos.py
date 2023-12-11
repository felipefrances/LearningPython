# #Example 1
#
# from flask import Flask
#
# app = Flask(__name__)
#
# @app.route("/")
# def home():
#     return "Olá! Aula de Algoritmos usando Flask <h1>Criando Páginas com Flask</h1> "
#
# if __name__ == "__main__":
#     app.run()
#
#
#
# ##################################################
#
# #Example 2
#
#
# from flask import Flask
#
# app = Flask(__name__)
#
# @app.route("/")
# def home():
#     return "Olá! Aula de Algoritmos usando Flask <h1>Criando Páginas com Flask</h1> "
#
#
# @app.route("/cadastrodealunos")
# def cadastrodealunos():
#     return " Cadastro de Alunos! <h1>Esta tela está reservada para construir a página de cadastro de alunos</h1>"
#
# if __name__ == "__main__":
#     app.run()
#
#
#
#
# ####################################
#
#
# #Example 3
#
# from flask import Flask
#
# app = Flask(__name__)
#
# @app.route("/")
# def home():
#     return "Hello! This is the main page <h1>HELLO</h1> "
#
# @app.route("/cadastrodealunos")
# def cadastrodealunos():
#     return " Cadastro de Alunos! <h1>Esta tela está reservada para construir a página de cadastro de alunos</h1>"
#
# @app.route("/<name>")
# def user(name):
#     return f'Hello {name}!'
#
# if __name__ == "__main__":
#     app.run()
#
#
# ###############################
#
#
# from flask import Flask, redirect, url_for
#
# app = Flask(__name__)
#
# @app.route("/")
# def home():
#     return "Hello! This is the main page <h1>HELLO</h1> "
#
# @app.route("/cadastrodealunos")
# def cadastrodealunos():
#     return " Cadastro de Alunos! <h1>Esta tela está reservada para construir a página de cadastro de alunos</h1>"
#
# @app.route("/<name>")
# def user(name):
#     return f'Hello {name}!'
#
# @app.route("/admin")
# def admin():
#     return redirect((url_for("home")))
#
# if __name__ == "__main__":
#     app.run()
#
#
# #--------------------------------------------------------------
# #Example 5 - Usando Templates
#
#
# from flask import Flask, render_template
#
# app = Flask(__name__)
#
# @app.route("/")
# def home():
#     return render_template("index.html")
#
#
# @app.route("/<name>")
# def name(name):
#     return render_template("index.html", content=name, parametro=["ai", "ei", "ou"])
#
# if __name__ == "__main__":
#     app.run(debug=True)
#
#

# #----------------------------------------------------------------------
# #Example 6
#

from flask import Flask, render_template, redirect, url_for, request
# from ConexaoPostgres import Conexao

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        user = request.form["nome"]
        #Conexao(user, idade, matricula)
        #return redirect(url_for('name', usr=user))
        return redirect(url_for('name2', name=user))
    else:
        return render_template("login.html")

@app.route("/<usr>")
def name(usr):
    return f"<h1>{usr}</h1>"



@app.route("/<name>")
def name2(name):
    return render_template("index3.html", content=name, parametro=["ai", "ei", "ou"])

#Conexao('Euristenho')


if __name__ == "__main__":
    app.run(debug=True)
#
#
#
# ==================================================
#
#
#
# Index.html -> Deve ser colocado na pasta templates
#
#
# <!DOCTYPE html>
# <html lang="en">
# <head>
#     <meta charset="UTF-8">
#     <title>Treinando Algoritmos</title>
# </head>
# <body>
#     <h1>Exercícios com Algoritmos</h1>
#     <p>Olá {{content}}</p>
# </body>
# </html>

