from flask import Flask, json, jsonify
from flask import request
from evento import Show
from playhouse.shortcuts import model_to_dict

app = Flask(__name__)

@app.route('/', methods=['GET'])
def inicio():
    return "backend do sistema de gerenciamento de festivais: <a href=/listar_itens>API listar itens</a>"

@app.route('/listar_itens')
def listar():
    shows = list(map(model_to_dict, Show.select()))
    return jsonify({"lista": shows})

app.run(debug=True, port=4999)
