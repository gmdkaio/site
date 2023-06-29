Maquinas = {
    "m1": {
        "nome": "maquina 1",
        "embalagem": [3, 4],
        "produto": [1, 2]
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

escolha_emb = 3
escolha_prod = 2
result = []

for x in Maquinas:
    if escolha_emb in Maquinas[x]["embalagem"] and escolha_prod in Maquinas[x]["produto"]:
        result.append(Maquinas[x]["nome"])
    else:
        pass

print(result)


