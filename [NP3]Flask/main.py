from flask import Flask, render_template, request, redirect, url_for
import psycopg2

app = Flask(__name__)

# Dados de exemplo para login
users = {'teste': '123', 'user2': 'password2'}


# Rota inicial
@app.route('/')
def login():
    return render_template('login.html')


# Rota após o login bem-sucedido
@app.route('/dashboard', methods=['POST'])
def dashboard():
    username = request.form['username']
    password = request.form['password']

    # Verifica se o usuário e a senha são válidos
    if username in users and users[username] == password:
        return render_template('dashboard.html', username=username)
    else:
        return redirect(url_for('login'))


# Rota de cadastro
@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    if request.method == "POST":
        user = request.form["nome"]
        idade = request.form["idade"]
        matricula = request.form["matricula"]

        conexao(user, idade, matricula)
        # return redirect(url_for('name', usr=user))
        return redirect(url_for('cadastrorealizado', name=user))
    else:
        return render_template('cadastro.html')


@app.route("/<name>")
def cadastrorealizado(name):
    return render_template("cadastrorealizado.html", content=name)


def conexao(user, idade, matricula):
    conectar = psycopg2.connect(database="postgres", user="postgres", password="123", host="localhost")
    cur = conectar.cursor()

    cur.execute(f"INSERT INTO alunos(nome, idade, matricula) VALUES ('{user}', {idade}, '{matricula}')")

    conectar.commit()
    cur.close()
    conectar.close()


if __name__ == '__main__':
    app.run(debug=True)
