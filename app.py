from flask import Flask, render_template, request, jsonify, session, make_response
import uuid, hashlib, secrets, json
from info.maquinas import Maquinas
from propostas import create_table_proposta, insert_proposta
from user_info import create_table_user, insert_info
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader
import io, os

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
        data = request.form.get('selected-date')

        user_id = session.get('user_id', None)
        session['versao'] = versao
        session['accessorios'] = accessorios
        session['produtos'] = produtos
        session['embalagens'] = embalagens
        session['data'] = data

        insert_proposta(app, user_id, versao, accessorios, produtos, embalagens, data)

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
    session['nome'] = nome
    session['endereco'] = endereco
    session['celular'] = celular
    session['email'] = email
    session['empresa'] = empresa
    session['cnpj'] = cnpj

    return jsonify(message='User information submitted successfully.')

def mp(px):
    return px * 0.352777

@app.route('/generate_pdf', methods=['POST'])
def generate_pdf():
    # Generate the PDF
    pdf_buffer = io.BytesIO()
    c = canvas.Canvas(pdf_buffer, pagesize=letter)

    # Header
    c.setFont("Helvetica", 20)
    hxl, hyl = mp(53), mp(2200)   # Upper left
    hxr, hyr = mp(1690), mp(2080)  # Lower right

    # Path to logo image 
    logo_image_path = os.path.join(app.root_path, 'static', 'images', 'pdf', 'logopdf.png')

    if os.path.exists(logo_image_path):
        c.drawImage(ImageReader(logo_image_path), x=mp(100), y=mp(2090), width=170, height=33)
    else:
        print(f"Logo image not found at '{logo_image_path}'. Please check the file path.")

    c.rect(hxl, hyl, hxr - hxl, hyr - hyl)
    c.setFont("Helvetica", 20)
    c.setFillColorRGB(255, 255, 255)  # Set the text color to white
    c.drawString(x=mp(1320), y=mp(2125), text='Maquina TP')

    # User info
    uxl, uyl = mp(53), mp(2060)   # Upper left
    uxr, uyr = mp(1690), mp(1500)  # Lower right  

    # Define the background color for the section below the top of the first section
    top_section_color = "#002d72"  # Background color for the section below the top

    # Manually apply the background color to the section below the top
    c.setFillColor(top_section_color)
    c.rect(uxl, uyl, uxr - uxl, mp(1985) - uyl, fill=True)

    # Define the background color for the section above the line
    bottom_section_color = "white"  # Background color for the section above the line

    # Manually apply the background color to the section above the line
    c.setFillColor(bottom_section_color)
    c.rect(uxl, mp(1985), uxr - uxl, uyr - mp(1985), fill=True)

    # Printing
    c.setFont("Helvetica", 12)  # Set the font size to 12 for the rest of the PDF
    c.setFillColorRGB(0, 0, 0)  # Set the text color to black

    c.rect(uxl, uyl, uxr - uxl, uyr - uyl)
    c.line(mp(53), mp(1985), mp(1690), mp(1985))

    # Draw a line separating the sections vertically
    midpoint_x = (mp(53) + mp(1690)) / 2
    c.line(midpoint_x, mp(2060), midpoint_x, mp(1500))

    # Top section user text color
    c.setFillColorRGB(255, 255, 255)
    c.drawString(x=mp(70), y=mp(2015), text='Informações do usuário')

    c.showPage()
    c.save()

    # Set up the response to download the PDF
    response = make_response(pdf_buffer.getvalue())
    response.headers['Content-Disposition'] = 'attachment; filename=sample.pdf'
    response.headers['Content-type'] = 'application/pdf'

    return response
    


if __name__ == '__main__':
    create_table_user(app)
    create_table_proposta(app)
    app.run()
