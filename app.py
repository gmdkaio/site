from email_sender import send_email_with_attachment, send_email_with_feedback, send_email_to_user
from flask import Flask, render_template, request, jsonify, session, make_response
from propostas import create_table_proposta, insert_proposta
import requests, hashlib, secrets, uuid, json, os, io, re
from user_info import create_table_user, insert_info
from reportlab.lib.utils import ImageReader
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from info.maquinas import Maquinas
from validate_docbr import CNPJ



secret_key = secrets.token_hex(16)

app = Flask(__name__, static_folder='static')
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

    session['embalagem_pdf'] = escolha_emb
    session['produto_pdf'] = escolha_prod

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
        return render_template(f'maquinas/maquina_selecionada.html', maquina=maquina_details)

    else:
        return render_template('404.html'), 404


@app.route('/completar_endereco', methods=['GET'])
def completar_endereco():
    cep = request.args.get('cep')
    
    if not cep:
        return jsonify({'error': 'Por favor, forneça um CEP'}), 400
    
    # Fazendo uma solicitação GET à API ViaCEP
    url = f'https://viacep.com.br/ws/{cep}/json/'
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        return jsonify(data)
    else:
        return jsonify({'error': 'CEP não encontrado'}), 404

@app.route('/product-info', methods=['POST'])
def product_info():
    descricao_produto = request.form.get('descricao_produto')
    peso_produto = request.form.get('peso_produto')
    unidade_peso = request.form.get('unidade_peso')

    session['descricao_produto'] = descricao_produto
    session['peso_produto'] = peso_produto
    session['unidade_peso'] = unidade_peso

    print('peso: ', peso_produto)
    print('unidade: ', unidade_peso)
    print('descricao: ', descricao_produto)
    
    return jsonify(message='Product information submitted successfully.')


@app.route('/proposta', methods=['GET', 'POST'])
def proposta():
    if request.method == 'POST':
        versao = request.form.get('version')
        accessorios = request.form.get('accessories')
        produtos = request.form.get('produtos')
        embalagens = request.form.get('embalagens')
        data = request.form.get('selected-date')
        linha = request.form.get('linha')

        peso = session.get('peso_produto')
        unidade_peso = session.get('unidade_peso')
        descricao = session.get('descricao_produto')

        print('peso: ', peso)
        print('unidade: ', unidade_peso)
        print('descricao: ', descricao)


        insert_proposta(app, versao, accessorios,
                        produtos, embalagens, data, descricao, peso, unidade_peso)
        
        session['versao'] = versao
        session['accessorios'] = accessorios
        session['produtos'] = produtos
        session['embalagens'] = embalagens
        session['data'] = data
        session['linha'] = linha
        
    # Generate the PDF
    pdf_buffer = io.BytesIO()
    c = canvas.Canvas(pdf_buffer, pagesize=letter)
    branco = "white"
    azul = "#002d72"
    preto = "black"
    cinza = "#ABAAAB"

    nome = session.get('nome', None)
    endereco = session.get('endereco', None)
    celular = session.get('celular', None)
    email = session.get('email', None)
    empresa = session.get('empresa', None)
    cnpj = session.get('cnpj', None)
    produtos = session.get('produto_pdf', None)
    embalagens = session.get('embalagem_pdf', None)

    if(produtos == 0):
       produtos = 'Não selecionado'
    elif(produtos == 1):
        produtos = 'Líquido'
    elif(produtos == 2):
        produtos == 'Viscoso'
    elif(produtos == 3):
        produtos == 'Pastoso'
    elif(produtos == 4):
        produtos = 'Pó'
    elif(produtos == 5):
        produtos == 'Granular'
    else:
        produtos == 'Sólido'

    if(embalagens == 0):
        embalagens = 'Não selecionado'
    elif(embalagens == 1):
        embalagens = 'Cartonada'
    elif(embalagens == 2):
        embalagens = 'Pouch'
    elif(embalagens == 3):
        embalagens = 'Especial'
    elif(embalagens == 4):
        embalagens = 'Sachê'
    elif(embalagens == 5):
        embalagens = 'Garrafa'
    elif(embalagens == 6):
        embalagens = 'Frasco'
    elif(embalagens == 7):
        embalagens = 'Fardo'   
    else:
        embalagens = 'Pote'  

    # Header
    c.setFont("Helvetica", 20)
    hxl, hyl = mp(53), mp(2200)   # Upper left
    hxr, hyr = mp(1690), mp(2080)  # Lower right

    # Path to logo image
    logo_image_path = os.path.join(
        app.root_path, 'static', 'images', 'pdf', 'logopdf.png')

    if os.path.exists(logo_image_path):
        c.drawImage(ImageReader(logo_image_path), x=mp(
            100), y=mp(2090), width=170, height=33)
    else:
        print(
            f"Logo image not found at '{logo_image_path}'. Please check the file path.")

    c.rect(hxl, hyl, hxr - hxl, hyr - hyl)
    c.setFont("Helvetica", 20)
    c.drawString(x=mp(1320), y=mp(2125), text=str(versao))

    # Info
    uxl, uyl = mp(53), mp(2060)   # Upper left
    uxr, uyr = mp(1690), mp(1650)  # Lower right

    # Manually apply the background color to the section below the top
    c.setFillColor(azul)
    c.rect(uxl, uyl, uxr - uxl, mp(1985) - uyl, fill=True)

    # Manually apply the background color to the section above the line
    c.setFillColor(branco)
    c.rect(uxl, mp(1985), uxr - uxl, uyr - mp(1985), fill=True)

    # Printing
    # Set the font size to 12 for the rest of the PDF
    c.setFont("Helvetica", 12)
    c.setFillColor(preto)  # Set the text color to black

    c.rect(uxl, uyl, uxr - uxl, uyr - uyl)
    c.line(mp(53), mp(1985), mp(1690), mp(1985))

    # Draw a line separating the sections vertically
    midpoint_x = (mp(53) + mp(1690)) / 2
    c.line(midpoint_x, mp(2060), midpoint_x, mp(1650))

    # Top section user text color
    c.setFont("Helvetica", 12)
    c.setFillColor(branco)
    c.drawString(x=mp(70), y=mp(2015), text='Informações do usuário')
    c.drawString(x=mp(890), y=mp(2015), text='Informações da proposta')

    # User info
    c.setFont("Helvetica", 12)
    c.setFillColor(preto)
    c.drawString(x=mp(70), y=mp(1930), text='Nome: ' + str(nome))
    c.drawString(x=mp(70), y=mp(1880), text='Celular: ' + str(celular))
    c.drawString(x=mp(70), y=mp(1830), text='Email: ' + str(email))
    c.drawString(x=mp(70), y=mp(1780), text='Empresa: ' + str(empresa))
    c.drawString(x=mp(70), y=mp(1730), text='Endereço: ' + str(endereco))
    c.drawString(x=mp(70), y=mp(1680), text='CNPJ: ' + str(cnpj))

    # selected machine info
    c.drawString(x=mp(890), y=mp(1930), text='Linha: ' + str(linha))
    c.drawString(x=mp(890), y=mp(1880), text='Máquina: ' + str(versao))
    c.drawString(x=mp(890), y=mp(1830), text='Produto: ' + str(produtos))
    c.drawString(x=mp(890), y=mp(1780), text='Embalagem: ' + str(embalagens))
    c.drawString(x=mp(890), y=mp(1730), text='Data da proposta: ' + str(data))

    #acessories info
    axl, ayl = mp(1130), mp(1630) # Upper right
    axr, ayr = mp(1690), mp(200) # Lower right

    c.setFillColor(azul)
    c.rect(axl, ayl, axr - axl, mp(1555) - ayl, fill=True)

    c.setFont("Helvetica", 12)
    c.setFillColor(branco)
    c.drawString(x=mp(1147), y=mp(1585), text='Acessórios')

    selected_accessories = accessorios
    if selected_accessories:
        accessories_list = selected_accessories.split('\n')
        y_offset = mp(1500)  # Starting y-coordinate for the first accessory
        line_spacing = mp(50)  # Spacing between lines
        for accessory in accessories_list:
            accessory = accessory.strip()  # Remove leading/trailing whitespace, including the newline character
            c.setFont("Helvetica", 12)
            c.setFillColor(preto)
            c.drawString(x=mp(1147), y=y_offset, text=accessory)
            y_offset -= line_spacing  # Move the next line up by the line_spacing value
    else:
        c.setFont("Helvetica", 12)
        c.setFillColor(preto)
        c.drawString(x=mp(1147), y=mp(1500), text='Nenhum acessório selecionado.')

    c.rect(axl, ayl, axr - axl, ayr - ayl)

    # machine info
    mxl, myl = mp(53), mp(1630)   # Upper left
    mxr, myr = mp(1120), mp(200)  # Lower right  

    c.rect(mxl, myl, mxr - mxl, myr - myl)

    # Footer
    fxl, fyl = mp(53), mp(180)
    fxr, fyr = mp(1690), mp(10)

    c.rect(fxl, fyl, fxr - fxl, fyr - fyl)

    icon_cell = os.path.join(app.root_path, 'static',
                             'images', 'pdf', 'telefone.png')
    icon_local = os.path.join(app.root_path, 'static',
                              'images', 'pdf', 'local.png')

    if os.path.exists(icon_cell):
        c.drawImage(ImageReader(icon_cell), x=mp(75), y=mp(35), width=40, height=40)
    else:
        print(
            f"Icon image not found at '{icon_cell}'. Please check the file path.")

    if os.path.exists(icon_local):
        c.drawImage(ImageReader(icon_local), x=mp(1100), y=mp(35), width=40, height=40)
    else:
        print(
            f"Icon image not found at '{icon_local}'. Please check the file path.")

    c.setFillColor(cinza)
    c.setFont("Helvetica", 12)
    c.drawString(x=mp(205), y=mp(77), text='+55 (41) 9 99674-8465')

    c.setFont("Helvetica", 9)
    c.drawString(x=mp(1210), y=mp(112),
                 text='Rua Marechal Deodoro 717 - 4º Andar')
    c.drawString(x=mp(1210), y=mp(82), text='Edifício Muralha - Centro')
    c.drawString(x=mp(1210), y=mp(
        52), text='CEP: 80020-320. Curitiba - PR, Brasil')

    c.showPage()
    c.save()

    pdf_content = pdf_buffer.getvalue()

    # Construct the email content using session variables
    email_content= {
        'nome': nome,
        'celular': celular,
        'email': email,
        'empresa': empresa,
    }

    send_email_with_attachment(pdf_content, email_content)

    return render_template('proposta.html')

def mp(px):
    return px * 0.352777

@app.route('/update_cookies', methods=['POST'])
def update_cookies():
    cookies_data = request.get_json()
    cookiesAccepted = cookies_data.get('cookiesAccepted', False)
    
    print('Cookies accepted: ', cookiesAccepted)
    
    return jsonify({'message': 'Cookies information received.'})


@app.route('/user-info', methods=['POST'])
def user_info():
    nome = request.form.get('nome')
    endereco = request.form.get('endereco')
    celular = request.form.get('celular')
    email = request.form.get('email')
    empresa = request.form.get('empresa')
    cnpj = request.form.get('cnpj', '')
    cep = request.form.get('cep', '')
    numero = request.form.get('numero', '')
    cidade = request.form.get('cidade', '')
    estado = request.form.get('estado', '')
    pais = request.form.get('pais', '')

    insert_info(app, nome, endereco, celular, email, empresa, cnpj, cep, numero, cidade, estado, pais)

    session['nome'] = nome
    session['endereco'] = endereco
    session['celular'] = celular
    session['email'] = email
    session['empresa'] = empresa
    session['cnpj'] = cnpj

    return jsonify(message='User information submitted successfully.')

@app.route('/download_pdf', methods=['POST'])
def download_pdf():
    # Generate the PDF
    pdf_bufferDownload = io.BytesIO()
    c = canvas.Canvas(pdf_bufferDownload, pagesize=letter)
    branco = "white"
    azul = "#002d72"
    preto = "black"
    cinza = "#ABAAAB"

    # variables
    nome = session.get('nome', None)
    endereco = session.get('endereco', None)
    celular = session.get('celular', None)
    email = session.get('email', None)
    empresa = session.get('empresa', None)
    cnpj = session.get('cnpj', None)
    versao = session.get('versao', None)
    accessorios = session.get('accessorios', None)
    produtos = session.get('produto_pdf', None)
    embalagens = session.get('embalagem_pdf', None)
    data = session.get('data', None)
    linha = session.get('linha', None)

    if(produtos == 0):
       produtos = 'Não selecionado'
    elif(produtos == 1):
        produtos = 'Líquido'
    elif(produtos == 2):
        produtos == 'Viscoso'
    elif(produtos == 3):
        produtos == 'Pastoso'
    elif(produtos == 4):
        produtos = 'Pó'
    elif(produtos == 5):
        produtos == 'Granular'
    else:
        produtos == 'Sólido'

    if(embalagens == 0):
        embalagens = 'Não selecionado'
    elif(embalagens == 1):
        embalagens = 'Cartonada'
    elif(embalagens == 2):
        embalagens = 'Pouch'
    elif(embalagens == 3):
        embalagens = 'Especial'
    elif(embalagens == 4):
        embalagens = 'Sachê'
    elif(embalagens == 5):
        embalagens = 'Garrafa'
    elif(embalagens == 6):
        embalagens = 'Frasco'
    elif(embalagens == 7):
        embalagens = 'Fardo'   
    else:
        embalagens = 'Pote'  

    # Header
    c.setFont("Helvetica", 20)
    hxl, hyl = mp(53), mp(2200)   # Upper left
    hxr, hyr = mp(1690), mp(2080)  # Lower right

    # Path to logo image
    logo_image_path = os.path.join(
        app.root_path, 'static', 'images', 'pdf', 'logopdf.png')

    if os.path.exists(logo_image_path):
        c.drawImage(ImageReader(logo_image_path), x=mp(
            100), y=mp(2090), width=170, height=33)
    else:
        print(
            f"Logo image not found at '{logo_image_path}'. Please check the file path.")

    c.rect(hxl, hyl, hxr - hxl, hyr - hyl)
    c.setFont("Helvetica", 20)
    c.drawString(x=mp(1320), y=mp(2125), text=str(versao))

    # Info
    uxl, uyl = mp(53), mp(2060)   # Upper left
    uxr, uyr = mp(1690), mp(1650)  # Lower right

    # Manually apply the background color to the section below the top
    c.setFillColor(azul)
    c.rect(uxl, uyl, uxr - uxl, mp(1985) - uyl, fill=True)

    # Manually apply the background color to the section above the line
    c.setFillColor(branco)
    c.rect(uxl, mp(1985), uxr - uxl, uyr - mp(1985), fill=True)

    # Printing
    # Set the font size to 12 for the rest of the PDF
    c.setFont("Helvetica", 12)
    c.setFillColor(preto)  # Set the text color to black

    c.rect(uxl, uyl, uxr - uxl, uyr - uyl)
    c.line(mp(53), mp(1985), mp(1690), mp(1985))

    # Draw a line separating the sections vertically
    midpoint_x = (mp(53) + mp(1690)) / 2
    c.line(midpoint_x, mp(2060), midpoint_x, mp(1650))

    # Top section user text color
    c.setFont("Helvetica", 12)
    c.setFillColor(branco)
    c.drawString(x=mp(70), y=mp(2015), text='Informações do usuário')
    c.drawString(x=mp(890), y=mp(2015), text='Informações da proposta')

    # User info
    c.setFont("Helvetica", 12)
    c.setFillColor(preto)
    c.drawString(x=mp(70), y=mp(1930), text='Nome: ' + str(nome))
    c.drawString(x=mp(70), y=mp(1880), text='Celular: ' + str(celular))
    c.drawString(x=mp(70), y=mp(1830), text='Email: ' + str(email))
    c.drawString(x=mp(70), y=mp(1780), text='Empresa: ' + str(empresa))
    c.drawString(x=mp(70), y=mp(1730), text='Endereço: ' + str(endereco))
    c.drawString(x=mp(70), y=mp(1680), text='CNPJ: ' + str(cnpj))

    # selected machine info
    c.drawString(x=mp(890), y=mp(1930), text='Linha: ' + str(linha))
    c.drawString(x=mp(890), y=mp(1880), text='Máquina: ' + str(versao))
    c.drawString(x=mp(890), y=mp(1830), text='Produto: ' + str(produtos))
    c.drawString(x=mp(890), y=mp(1780), text='Embalagem: ' + str(embalagens))
    c.drawString(x=mp(890), y=mp(1730), text='Data da proposta: ' + str(data))

    #acessories info
    axl, ayl = mp(1130), mp(1630) # Upper right
    axr, ayr = mp(1690), mp(200) # Lower right

    c.setFillColor(azul)
    c.rect(axl, ayl, axr - axl, mp(1555) - ayl, fill=True)

    c.setFont("Helvetica", 12)
    c.setFillColor(branco)
    c.drawString(x=mp(1147), y=mp(1585), text='Acessórios')

    selected_accessories = accessorios
    if selected_accessories:
        accessories_list = selected_accessories.split('\n')
        y_offset = mp(1500)  # Starting y-coordinate for the first accessory
        line_spacing = mp(50)  # Spacing between lines
        for accessory in accessories_list:
            accessory = accessory.strip()  # Remove leading/trailing whitespace, including the newline character
            c.setFont("Helvetica", 12)
            c.setFillColor(preto)
            c.drawString(x=mp(1147), y=y_offset, text=accessory)
            y_offset -= line_spacing  # Move the next line up by the line_spacing value
    else:
        c.setFont("Helvetica", 12)
        c.setFillColor(preto)
        c.drawString(x=mp(1147), y=mp(1500), text='Nenhum acessório selecionado.')

    c.rect(axl, ayl, axr - axl, ayr - ayl)

    # machine info
    mxl, myl = mp(53), mp(1630)   # Upper left
    mxr, myr = mp(1120), mp(200)  # Lower right  

    c.rect(mxl, myl, mxr - mxl, myr - myl)

    # Footer
    fxl, fyl = mp(53), mp(180)
    fxr, fyr = mp(1690), mp(10)

    c.rect(fxl, fyl, fxr - fxl, fyr - fyl)

    icon_cell = os.path.join(app.root_path, 'static',
                             'images', 'pdf', 'telefone.png')
    icon_local = os.path.join(app.root_path, 'static',
                              'images', 'pdf', 'local.png')

    if os.path.exists(icon_cell):
        c.drawImage(ImageReader(icon_cell), x=mp(
            75), y=mp(35), width=40, height=40)
    else:
        print(
            f"Icon image not found at '{icon_cell}'. Please check the file path.")

    if os.path.exists(icon_local):
        c.drawImage(ImageReader(icon_local), x=mp(
            1100), y=mp(35), width=40, height=40)
    else:
        print(
            f"Icon image not found at '{icon_local}'. Please check the file path.")

    c.setFillColor(cinza)
    c.setFont("Helvetica", 12)
    c.drawString(x=mp(205), y=mp(77), text='+55 (41) 9 99674-8465')

    c.setFont("Helvetica", 9)
    c.drawString(x=mp(1210), y=mp(112),
                 text='Rua Marechal Deodoro 717 - 4º Andar')
    c.drawString(x=mp(1210), y=mp(82), text='Edifício Muralha - Centro')
    c.drawString(x=mp(1210), y=mp(
        52), text='CEP: 80020-320. Curitiba - PR, Brasil')

    c.showPage()
    c.save()

    pdf_contentDownload = pdf_bufferDownload.getvalue()


    # Set up the response to download the PDF
    response = make_response(pdf_contentDownload)
    response.headers['Content-Disposition'] = 'attachment; filename=solicitação.pdf'
    response.headers['Content-type'] = 'application/pdf'

    return response

@app.route('/send_feedback', methods=['POST'])
def send_feedback():
    feedback_data = request.get_json()
    feedback_content = feedback_data.get('feedback')

    nome = session.get('nome', None)
    email = session.get('email', None)

    email_content= {
        'nome': nome,
        'email': email,
    }

    send_email_with_feedback(feedback_content, email_content)
    return jsonify({"message": "Enviado"})

if __name__ == '__main__':
    create_table_user(app)
    create_table_proposta(app)
    app.run(debug=True)