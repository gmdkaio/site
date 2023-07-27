from flask import Flask, render_template, request, jsonify, session
import uuid, hashlib, secrets, json
from info.maquinas import Maquinas
from propostas import create_table_proposta, insert_proposta
from user_info import create_table_user, insert_info
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet

secret_key = secrets.token_hex(16)

app = Flask(__name__)
DATABASE = 'propostas.db'
DATABASE_USERS = 'user_info.db'
app.secret_key = secret_key


with app.app_context():
    create_table_proposta(app)
    create_table_user(app)
    

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
        versao = request.form.get('version')
        accessorios = request.form.get('accessories')
        produtos = request.form.get('produtos')
        embalagens = request.form.get('embalagens')

        user_id = session.get('user_id', None)

        insert_proposta(app, user_id, versao, accessorios, produtos, embalagens)

        return render_template('proposta.html', version=versao, accessories=accessorios, produtos=produtos, embalagens=embalagens)

    return render_template('proposta.html')

@app.route('/user-info', methods=['POST'])
def user_info():
    nome = request.form.get('nome')
    endereco = request.form.get('endereco')
    celular = request.form.get('celular')
    email = request.form.get('email')
    empresa = request.form.get('empresa')
    cnpj = request.form.get('cnpj', '')  

    uuid_hash = hashlib.sha1(str(uuid.uuid4()).encode()).hexdigest()[:5]
    user_id = uuid_hash

    insert_info(app, user_id, nome, endereco, celular, email, empresa, cnpj)

    session['user_id'] = user_id

    return jsonify(message='User information submitted successfully.')

# def generate_pdf():
#     d

if __name__ == '__main__':
    create_table_user(app)
    create_table_proposta(app)
    app.run()
