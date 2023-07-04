from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

Maquinas = {
    "m1": {
        "nome": "maquina 1",
        "embalagem": [3, 4],
        "produto": [1, 2],
    },
    "m2": {
        "nome": "maquina 2",
        "embalagem": [2, 1],
        "produto": [2, 3]
    },
    "m3": {
        "nome": "maquina 3",
        "embalagem": [4, 5],
        "produto": [1, 3]
    },
    "m4": {
        "nome": "maquina 4",
        "embalagem": [4, 1],
        "produto": [4, 2]
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