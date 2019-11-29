from flask import Flask, json, jsonify
from flask import request
from evento import Integrante
from playhouse.shortcuts import model_to_dict

app = Flask(__name__)

@app.route('/', methods=['GET'])
def inicio():
    return "backend do sistema de gerenciamento de festivais: <a href=/listar_itens>API listar itens</a>"

@app.route('/listar_itens')
def listar():
    integrantes = list(map(model_to_dict, Integrante.select()))
    return jsonify({"lista": integrantes})

app.run(debug=True, port=4999)
