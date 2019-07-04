from pessoa import *
from flask import *
from peewee import *

app = Flask(__name__)

app.config['SECRET KEY'] = 'admin'

@app.route("/")
def iniciar():
    return render_template("inicio.html")

@app.route('/listar')
def listar():
    return render_template('listar.html', users=Pessoa.select())

@app.route('/inserir')
def inserir():
    cpf = int(request.args.get("cpf"))
    nome = request.args.get("nome")
    Pessoa.create(cpf = cpf, nome = nome)
    return redirect(url_for('iniciar'))

@app.route("/form_alterar")
def form_alterar():
    quem = Pessoa.get_by_id(request.args.get("cpf"))
    return render_template('form_alterar.html', achei = quem)

@app.route("/alterar")
def alterar():
    quem = Pessoa.get_by_id(request.args.get("cpf"))
    quem.nome = request.args.get("nome")
    quem.save()
    return redirect(url_for('iniciar'))

@app.route('/excluir')
def excluir():
    Pessoa.delete_by_id(request.args.get("cpf"))
    return render_template("inicio.html")


@app.route('/login', methods = ['post'])
def login():
    login = request.form['login']
    senha = request.form['senha']

    if login=='admin' and senha=='123':
        session['usuario'] = login
        return redirect('/')
    else:
        return "erroooo"

@app.route('/logout')
def logout():
    session.pop('usuario')
    return redirect('/')

app.run()

