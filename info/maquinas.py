# Embalagens:

# 1 - Gable Top
# 2 - Stand-up Pouch
# 3 - Especial
# 4 - Sachê
# 5 - Garrafa
# 6 - Frasco
# 7 - Fardo
# 8 - Pote

# Produtos:

# 1 - Líquido
# 2 - Viscoso
# 3 - Pastoso
# 4 - Pó
# 5 - Granular
# 6 - Sólido


Maquinas = {
    
  'TP': {
      'linha': 'Linha TP',
      'nome': 'Linha TP',
      'embalagem': [3, 4],
      'produto': [1, 2, 3, 4, 5, 6],
      'imagem': '../static/images/maquinas/tp.jpg',
      'descricao': 'Máquinas envasadoras da linha TP',
      'pagina': 'maquina-tp',
      'acessorios': []
    },

    'TC 4S': {
        'linha': 'Linha TC 4S',
        'nome': 'Linha TC 4S',
        'embalagem': [3, 4],
        'produto': [1, 2, 3, 4, 5, 6],
        'imagem': '../static/images/maquinas/tc4S-1.jpg',
        'descricao': 'Máquinas envasadoras da linha TC 4S',
        'pagina': 'maquina-tc4s',
        'acessorios': []
    },

    'TC 3SC PÓ E SÓLIDOS': {
        'linha': 'Linha TC 3SC',
        'nome': 'Linha 3SC Pó e sólidos',
        'embalagem': [3, 4],
        'produto': [4, 5, 6],
        'imagem': '../static/images/maquinas/tC3S_po_solidos.jpg',
        'descricao': 'Máquinas envasadoras da linha TC3SC Pós e sólidos',
        'pagina': 'maquina-tc3scps',
        'acessorios': []
    },

    'TC 3SC LÍQUIDOS E SECOS': {
        'linha': 'Linha TC 3SC',
        'nome': 'Linha 3SC Líquidos e secos',
        'embalagem': [3, 4],
        'produto': [1, 2, 3, 4, 5, 6],
        'imagem': '../static/images/maquinas/tc-3SC_liquidos_secos.jpg',
        'descricao': 'Máquinas envasadoras da linha TC3SC Líquidos e secos',
        'pagina': 'maquina-tc3scls',
        'acessorios': []
    },

    'TC 3SC STICK': {
        'linha': 'Linha TC 3SC',
        'nome': 'Linha TC 3SC Stick',
        'embalagem': [3, 4],
        'produto': [1, 2, 3, 4, 5, 6],
        'imagem': '../static/images/maquinas/tc-3SC-stick.jpg',
        'descricao': 'Máquinas envasadoras da linha TC3SC Stick',
        'pagina': 'maquina-tc3s',
        'acessorios': []
    },

    'TC-3SL': {
        'linha': 'Linha TC-3SL',
        'nome': 'Linha TC-3SL',
        'embalagem': [3, 4],
        'produto': [1, 2, 3, 4, 5, 6],
        'imagem': '../static/images/maquinas/tc-3SL.jpg',
        'descricao': 'Máquinas envasadoras da linha TC-3SL',
        'pagina': 'maquina-tc3sl',
        'acessorios': []
    },

    'FRASCOS LINEAR': {
        'linha': 'Linha de frascos',
        'nome': 'Linha de frascos linear',
        'embalagem': [5, 6],
        'produto': [1, 2, 3, 4, 5, 6],
        'imagem': '../static/images/maquinas/linha-frascos-1.jpg',
        'descricao': 'Máquinas envasadoras da linha de frascos linear',
        'pagina': 'maquina-frascoln',
        'acessorios': []
    },

    'FRASCOS TRIBLOCK': {
        'linha': 'Linha de frascos',
        'nome': 'Linha de frascos triblock',
        'embalagem': [5, 6],
        'produto': [1, 2, 3],
        'imagem': '../static/images/maquinas/linha-frascos-2.jpg',
        'descricao': 'Máquinas envasadoras da linha de frascos triblock',
        'pagina': 'maquina-frascotr',
        'acessorios': []
    },

    'FRASCOS ROTATIVA': {
        'linha': 'Linha de frascos',
        'nome': 'Linha de frascos rotativa',
        'embalagem': [5, 6],
        'produto': [1, 2, 3],
        'imagem': '../static/images/maquinas/linha-frascos-3.jpg',
        'descricao': 'Máquinas envasadoras da linha de frascos rotativa',
        'pagina': 'maquina-frascortv',
        'acessorios': []
    },

    'FRASCOS SPEED': {
        'linha': 'Linha de frascos',
        'nome': 'Linha de frascos rotativa speed',
        'embalagem': [5, 6],
        'produto': [1, 2, 3],
        'imagem': '../static/images/maquinas/linha-frascos-4.jpg',
        'descricao': 'Máquinas envasadoras da linha de frascos rotativa speed',
        'pagina': 'maquina-frascorts',
        'acessorios': []
    },

    'POTES': {
        'linha': 'Linha de potes',
        'nome': 'Linha de potes',
        'embalagem': [8],
        'produto': [1, 2, 3, 4, 5, 6],
        'imagem': '../static/images/maquinas/linha-potes.jpg',
        'descricao': 'Máquinas envasadoras da linha de potes',
        'pagina': 'maquina-potes',
        'acessorios': []
    },

    'TC 4BC': {
        'linha': 'Linha TC 4B',
        'nome': 'Linha TC 4B',
        'embalagem': [2, 3],
        'produto': [1, 2, 3, 4, 5, 6],
        'imagem': '../static/images/maquinas/stand-up-pouch-1.jpg',
        'descricao': 'Máquinas envasadoras da linha TC 4BC',
        'pagina': 'maquina-tc4bc',
        'acessorios': []
    },

    'POUCH': {
        'linha': 'Linha Pouch',
        'nome': 'Linha Pouch pronto',
        'embalagem': [2, 3],
        'produto': [1, 2, 3, 4, 5, 6],
        'imagem': '../static/images/maquinas/pouch-pronto.jpg',
        'descricao': 'Máquinas envasadoras da linha pouch pronto',
        'pagina': 'maquina-pouch',
        'acessorios': []
    },

    'TC SUP': {
        'linha': 'Linha TC SUP',
        'nome': 'Linha TC SUP',
        'embalagem': [2, 3],
        'produto': [1, 2],
        'imagem': '../static/images/maquinas/mini-pouch.jpg',
        'descricao': 'Máquinas envasadoras da linha TC SUP',
        'pagina': 'maquina-tcsup',
        'acessorios': []
    },

    'TC 4U': {
        'linha': 'Linha TC 4U',
        'nome': 'Linha TC 4U',
        'embalagem': [7],
        'produto': [6],
        'imagem': '../static/images/maquinas/tc-4u.jpg',
        'descricao': 'Máquinas enfardadeiras da linha TC 4U',
        'pagina': 'maquina-tc4u',
        'acessorios': []
    }, 

    'PTC': {
        'linha': 'Linha PTC',
        'nome': 'Linha PTC',
        'embalagem': [3, 4],
        'produto': [4, 5, 6],
        'imagem': '../static/images/maquinas/ptc.jpg',
        'descricao': 'Máquinas embaladoras da linha PTC',
        'pagina': 'maquina-ptc',
        'acessorios': []
    },

    'TC 3SC BAG': {
        'linha': 'Linha TC 3SC BAG',
        'nome': 'Linha TC 3SC BAG',
        'embalagem': [3, 4],
        'produto': [1, 2],
        'imagem': '../static/images/maquinas/tc3SC.jpg',
        'descricao': 'Máquinas envasadoras da linha TC 3SC BAG',
        'pagina': 'maquina-tc3scb',
        'acessorios': []
    },

    'FLOWPACK': {
        'linha': 'Linha Flowpack',
        'nome': 'Linha Flowpack',
        'embalagem': [3, 4],
        'produto': [6],
        'imagem': '../static/images/maquinas/flowpack.jpg',
        'descricao': 'Máquinas envasadoras da linha flowpack',
        'pagina': 'maquina-flowpack',
        'acessorios': []
    },

    'BISNAGAS': {
        'linha': 'Linha bisnagas',
        'nome': 'Linha bisnagas',
        'embalagem': [6],
        'produto': [1, 2],
        'imagem': '../static/images/maquinas/linha-bisnagas.jpg',
        'descricao': 'Máquinas envasadoras da linha bisnagas',
        'pagina': 'maquina-bisnaga',
        'acessorios': []
    },

    'CARTONADAS': {
        'linha': 'Linha cartonadas',
        'nome': 'Linha embalagens cartonadas',
        'embalagem': [1],
        'produto': [1, 2, 3, 4, 5, 6],
        'imagem': '../static/images/maquinas/linha-embalagem-cartonada.jpg',
        'descricao': 'Máquinas envasadoras da linha cartonada',
        'pagina': 'maquina-cartonada',
        'acessorios': []
    },

    'GALOES': {
        'linha': 'Linha de galões',
        'nome': 'Linha de galões',
        'embalagem': [5],
        'produto': [1],
        'imagem': '../static/images/maquinas/linha-galoes.jpg',
        'descricao': 'Máquinas da linha de galões',
        'pagina': 'maquina-galao',
        'acessorios': []
    },

    'PET': {
        'linha': 'Linha PET',
        'nome': 'Pet com túnel',
        'embalagem': [5],
        'produto': [6],
        'imagem': '../static/images/maquinas/pet-com-tunel.jpg',
        'descricao': 'Máquinas envolvedoras da linha PET com túnel',
        'pagina': 'maquina-pet',
        'acessorios': []
    }
}