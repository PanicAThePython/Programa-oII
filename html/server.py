from flask import Flask, render_template, request, redirect, url_for
from pessoa import *
app = Flask("__name__")

@app.route("/")
def iniciar():
    return render_template("inicio.html")

@app.route("/listar_pessoas")
def listar_pessoas():
    return render_template("listar_pessoas.html", usuarios=lista)

@app.route("/inserir_pessoa")
def inserir_pessoa():
    return render_template("inserir_pessoa.html")

@app.route("/exibir_mensagem")
def exibir_mensagem():
    return render_template("exibir_mensagem.html")

@app.route("/processar_inserir")
def add():
    cpf = int(request.args.get("cpf"))
    nome = request.args.get("nome")
    endereco = request.args.get("endereco")
    telefone = request.args.get("telefone")
    lista.append(Pessoa(cpf,nome,endereco,telefone))
    return redirect(url_for("iniciar"))
   

@app.route("/excluir_pessoa")
def excluir():

    chave = int(request.args.get("cpf"))

    for p in lista:
        if p.cpf == chave:
            lista.remove(p)

    return redirect(url_for("listar_pessoas"))

@app.route("/form_alterar_pessoa")
def form_alterar_pessoa():
    
    chave = request.args.get("cpf")
    print(chave)

    for p in lista:
        if p.cpf == int(chave):
            return render_template("form_alterar_pessoa.html", achei=p)
    return "Pessoa não encontrada"

@app.route("/alterar_pessoa")
def alterar_pessoa():
    cpf = int(request.args.get("cpf"))
    nome = request.args.get("nome")
    telefone = request.args.get("telefone")
    endereco = request.args.get("endereco")

    for i in range(len(lista)):
        if lista[i].cpf == cpf:
            lista[i] = Pessoa(cpf,nome,endereco,telefone)
            return redirect(url_for("listar_pessoas"))
    return "Não achei, desculpe!"

app.run()