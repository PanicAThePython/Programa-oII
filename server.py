from flask import Flask, render_template, request, redirect, url_for, session
from pessoa import *
from peewee import *

app = Flask("__name__") #objeto

app.config["SECRET_KEY"] = 'admin'
@app.route("/")
def iniciar():
    return render_template("inicio.html") #render_template: renderiza a pagina web

@app.route("/listar_pessoas")
def listar_pessoas():
    return render_template("listar_pessoas.html", usuarios=Pessoa.select())

@app.route("/form_inserir_pessoa")
def inserir_pessoa():
    return render_template("inserir_pessoa.html")

@app.route("/exibir_mensagem")
def exibir_mensagem():
    return render_template("exibir_mensagem.html")

@app.route("/processar_inserir", methods=['post'])
def add():
    cpf = int(request.form["cpf"])
    nome = request.form["nome"]
    endereco = request.form["endereco"]
    telefone = request.form["telefone"]
    Pessoa.create(cpf = cpf, nome = nome, endereco = endereco, telefone = telefone)
    return redirect(url_for("iniciar"))
    

@app.route("/excluir_pessoa")
def excluir():

    chave = int(request.args.get("cpf"))

    for p in lista:
        if p.cpf == chave:
            lista.remove(p)
    
    return redirect("/listar_pessoas")

@app.route("/form_alterar_pessoa")
def form_alterar_pessoa():
    
    chave = request.args.get("cpf")
    
    for p in lista:
        if p.cpf == int(chave):
            return render_template("form_alterar_pessoa.html", achei=p)
    return "Pessoa não encontrada"

@app.route("/alterar_pessoa", methods=['post'])
def alterar_pessoa():
    cpf = int(request.form["cpf"])
    nome = request.form["nome"]
    telefone = request.form["telefone"]
    endereco = request.form["endereco"]

    for i in range(len(lista)):
        if lista[i].cpf == cpf:
            lista[i] = Pessoa(cpf,nome,endereco,telefone)
            return redirect(url_for("listar_pessoas"))
    return "Não achei, desculpe!"

@app.route("/form_login")
def form_login():
    return render_template("form_login.html")

@app.route("/login", methods=['post'])
def login():
    login = request.form["login"]
    senha = request.form["senha"]

    if login == "admin" and senha == "admin":
        session['usuario'] = login
        return redirect("/")
    else:
        return "erro no login, tente novamente"

@app.route("/logout")
def logout():
    session.pop("usuario")
    return redirect("/")

app.run()
