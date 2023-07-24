from flask import Flask, render_template, request, jsonify
import json
from info.maquinas import Maquinas
from database import create_table, insert_proposta, close_connection

app = Flask(__name__)
DATABASE = 'propostas.db'

with app.app_context():
    create_table(app)

@app.route('/', methods=['GET'])
def index():
    maquinas_json = json.dumps(Maquinas)
    return render_template('index.html', maquinas=maquinas_json)


@app.route('/filter', methods=['POST'])
def filter_maquinas():

    escolha_emb = int(request.form.get('embalagem', 0))
    escolha_prod = int(request.form.get('produto', 0))
    result = []

    for key in Maquinas:
        embalagem_match = escolha_emb in Maquinas[key]["embalagem"]
        produto_match = escolha_prod in Maquinas[key]["produto"]

        if escolha_emb and escolha_prod:
            if embalagem_match and produto_match:
                result.append(key)
        elif escolha_emb:
            if embalagem_match:
                result.append(key)
        elif escolha_prod:
            if produto_match:
                result.append(key)

    return jsonify(result=result)


@app.route('/maquinas/<maquina_pagina>', methods=['GET'])
def maquina_page(maquina_pagina):
    maquina_details = None
    for key, value in Maquinas.items():
        if value.get('pagina') == maquina_pagina:
            maquina_details = value
            break

    if maquina_details:
        return render_template(f'maquinas/{maquina_pagina}.html', maquina=maquina_details)

    else:
        return render_template('404.html'), 404

@app.route('/proposta', methods=['GET', 'POST'])
def proposta():
    if request.method == 'POST':
        version = request.form.get('version')
        accessories = request.form.get('accessories')

        insert_proposta(app, version, accessories)

        return render_template('proposta.html', version=version, accessories=accessories)

    return render_template('proposta.html')

if __name__ == '__main__':
    create_table(app)
    app.run()
