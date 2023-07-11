from flask import Flask, render_template, request, jsonify
from info.maquinas import Maquinas

app = Flask(__name__)

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