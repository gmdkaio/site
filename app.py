from flask import Flask, render_template, request, jsonify

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


Maquinas = {
    "m1": {
        "nome": "maquina 1",
        "embalagem": [3, 4],
        "produto": [1, 2],
        "producao": 1000
    },
    "m2": {
        "nome": "maquina 2",
        "embalagem": [2, 1],
        "produto": [2, 3],
        "producao": 2000
    },
    "m3": {
        "nome": "maquina 3",
        "embalagem": [4, 5],
        "produto": [1, 3], 
        "producao": 3000
    },
    "m4": {
        "nome": "maquina 4",
        "embalagem": [4, 1],
        "produto": [4, 2],
        "producao": 4000
    }
}

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/filter', methods=['POST'])
def filter_maquinas():
    escolha_emb = int(request.form.get('embalagem', 0))
    escolha_prod = int(request.form.get('produto', 0))
    result = []

    for x in Maquinas:
        embalagem_match = escolha_emb in Maquinas[x]["embalagem"]
        produto_match = escolha_prod in Maquinas[x]["produto"]

        if escolha_emb and escolha_prod:
            if embalagem_match and produto_match:
                result.append(Maquinas[x]["nome"])
        elif escolha_emb:
            if embalagem_match:
                result.append(Maquinas[x]["nome"])
        elif escolha_prod:
            if produto_match:
                result.append(Maquinas[x]["nome"])

    return jsonify(result=result)

if __name__ == '__main__':
    app.run()