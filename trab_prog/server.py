from flask import Flask, json, jsonify
from flask import request
from evento import Ingresso
from playhouse.shortcuts import model_to_dict

# inicializa o servidor
app = Flask(__name__)


@app.route('/', methods=['GET'])
def inicio():
    return "backend do sistema de pessoas; <a href=/listar_itens>API listar itens</a>"


@app.route('/listar_itens')
def listar():
    # converte para pessoa para inserir em uma lista json
    ingressos = list(map(model_to_dict, Ingresso.select()))
    # adiciona à lista json um nome
    return jsonify({"lista": ingressos})

app.run(debug=True, port=4999)