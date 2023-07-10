from flask import Flask, render_template, request, jsonify
from linhas.maquinas import Maquinas

app = Flask(__name__)

# SISTEMA DE FILTROS               

# EMBALAGENS:

# 1 - GABLE TOP
# 2 - STAND-UP POUCH
# 3 - ESPECIAL
# 4 - SACHÊ
# 5 - GARRAFA
# 6 - FRASCO
# 7 - FARDO
# 8 - POTE

# PRODUTOS: 

# 1 - LÍQUIDO FINO
# 2 - LÍQUIDO MÉDIO
# 3 - LÍQUIDO GROSSO
# 4 - PÓ
# 5 - GRANULAR
# 6 - SÓLIDO


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/filter', methods=['POST'])
def filter_maquinas():

    #Pega o valor dos botôes
    escolha_emb = int(request.form.get('embalagem', 0))
    escolha_prod = int(request.form.get('produto', 0))
    result = []

    #Filtragem
    for x in Maquinas:
        embalagem_match = escolha_emb in Maquinas[x]['embalagem']
        produto_match = escolha_prod in Maquinas[x]['produto']

        if escolha_emb and escolha_prod:
            if embalagem_match and produto_match:
                result.append(Maquinas[x]['nome'])
        elif escolha_emb:
            if embalagem_match:
                result.append(Maquinas[x]['nome'])
        elif escolha_prod:
            if produto_match:
                result.append(Maquinas[x]['nome'])

    return jsonify(result=result)

if __name__ == '__main__':
    app.run()