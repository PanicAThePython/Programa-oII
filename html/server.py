from flask import Flask, render_template, request
from pessoa import *
app = Flask("__name__")

@app.route("/")
def iniciar():
    return render_template("inicio.html")

@app.route("/listar_pessoas")
def listar_pessoas():
    return render_template("listar_pessoas.html", usuarios=lista)

@app.route("/alterar_pessoa")
def alterar_pessoa():
    return render_template("alterar_pessoa.html")

@app.route("/inserir_pessoa")
def inserir_pessoa():
    return render_template("inserir_pessoa.html")

@app.route("/exibir_mensagem")
def exibir_mensagem():
    return render_template("exibir_mensagem.html")

@app.route("/processar_inserir")
def add():
    cpf = request.args.get("cpf")
    nome = request.args.get("nome")
    endereco = request.args.get("endereco")
    telefone = request.args.get("telefone")
    lista.append(Pessoa(cpf,nome,endereco,telefone))
    return listar_pessoas()

@app.route("/excluir_pessoa")
def excluir():

    chave = request.args.get("cpf")
    print(type(chave))
    
    for p in lista:
        if p.cpf == int(chave):
            lista.remove(p)
    

    return listar_pessoas()

app.run(host="0.0.0.0")