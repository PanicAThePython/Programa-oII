from flask import Flask, render_template

app = Flask("__name__")

@app.route("/")
def iniciar():
    return render_template("inicio.html")

@app.route("/listar_pessoas")
def listar_pessoas():
    return render_template("listar_pessoas.html")

@app.route("/alterar_pessoa")
def alterar_pessoa():
    return render_template("alterar_pessoa.html")

@app.route("/inserir_pessoa")
def inserir_pessoa():
    return render_template("inserir_pessoa.html")


@app.route("/exibir_mensagem")
def exibir_mensagem():
    return render_template("exibir_mensagem.html")

app.run(host="0.0.0.0")

