maquinas = {
    "m1": {

        "embalagem": 3,
        "produto": 1
    },

    "m2": {

        "embalagem": 2,
        "produto": 2
    },

    "m3": {

        "embalagem": 4,
        "produto": 3
    },

    "m4": {

        "embalagem": 1,
        "produto": 2
    }
}

escolha_embalagem = 1
escolha_produto = 2


def filtro_m(unit_num):
    if maquinas[unit_num]["embalagem"] == escolha_embalagem and maquinas[unit_num]["produto"] == escolha_produto:
        return True
    else:
        return False


x = list(filter(filtro_m, maquinas))

print(x)
