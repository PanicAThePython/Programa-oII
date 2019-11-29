from flask import Flask, json, jsonify
from flask import request
from evento import Musica
from playhouse.shortcuts import model_to_dict

app = Flask(__name__)

@app.route('/', methods=['GET'])
def inicio():
    return "backend do sistema de gerenciamento de festivais: <a href=/listar_itens>API listar itens</a>"

@app.route('/listar_itens')
def listar():
    musicas = list(map(model_to_dict, Musica.select()))
    return jsonify({"lista": musicas})

app.run(debug=True, port=4999)
