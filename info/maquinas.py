# Embalagens

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

Maquinas ={
    'TP':{
        'linha': 'Linha TP',
        'linha_texto':'A Linha TP de maquinas envasadoras para sache oferece envase preciso e rápido para uma variedade de produtos, de líquidos a secos, garantindo embalagens de alta qualidade, com ótimo selamento.',
        'nome': 'Linha TP',
        "variacao":'variam de acordo com o tamanho da embalagem',
        'embalagem': [3, 4],
        'modelos': ['TP 85' , 'TP 100', 'TP 120', 'TP 140', 'TP 180', 'TP 300'],
        'produto': [1, 2, 3, 4, 5, 6],
        'imagem': '../static/images/maquinas/tp-com-embalagem.jpg',
        'imagem_pag_maquina':'/static/images/maquinas/tp.png',
        'descricao': 'Máquinas envasadoras para sache 2 soldas, linha TP 80 a 340',
        'pagina': 'maquina-tp',
        'acessorios': [],
        'espessura_filme':' 60 a 90 [μm]',
        'material_embalagem':'PEBD e PEAD',
        'produto_texto':'Liquidos e Secos',
        'info_tecnicas':{
            'producao':'2.400',
            'datador':'Hotstamping',
            'dosagem':'Temporizado | Bomba Positiva | Volumétrico',
            'tensao':'220 [V] - 60 [Hz]',
            'potencia_instalada':'1,95 a 2,15',
            'potencia_consumida':'1,20 a 1,80',
            'comando':'CLP com IHM Touchscreen',
            'consumo_ar':'277[L/min]',
            'area':'2,1x2,45',
            'material':'Aço inoxidável AISI 304, alumínio, policarbonato e aço carbono'
        },
        'info_embalagem':{
            'variacao':'A altura dos saches pode ser personalizada',
            'TP85':{
                'largura':'85',
                'final':'35',
            },
            'TP100':{
                'largura':'100',
                'final':'45',
            },
            'TP120':{
                'largura':'120',
                'final':'55',
            },
            'TP140':{
                'largura':'140',
                'final':'65',
            },
            'TP180':{
                'largura':'180',
                'final':'80',
            },
            'TP300':{
                'largura':'85',
                'final':'140',
            },
        }
    },

    'TC 4S-1': {
        'linha': 'Linha TC',
        'nome': 'Linha TC 4S-1',
        'embalagem': [3, 4],
        'produto': [1, 2, 3, 4, 5, 6],
        'imagem': '../static/images/maquinas/tc4S-1-com-embalagem.jpg',
        'descricao': 'Máquinas envasadoras da linha TC 4S-1',
        'pagina': 'maquina-tc4s-1',
        'acessorios': []
    },
    
    'TC 4S-2': {
        'linha': 'Linha TC',
        'nome': 'Linha TC 4S-2',
        'embalagem': [3, 4],
        'produto': [1, 2, 3, 4, 5, 6],
        'imagem': '../static/images/maquinas/tc4S-2-com-embalagem.jpg',
        'descricao': 'Máquinas envasadoras da linha TC 4S-2',
        'pagina': 'maquina-tc4s-2',
        'acessorios': []
    },

        'TC 4S-3': {
        'linha': 'Linha TC',
        'nome': 'Linha TC 4S-3',
        'embalagem': [3, 4],
        'produto': [1, 2, 3, 4, 5, 6],
        'imagem': '../static/images/maquinas/tc4S-3-com-embalagem.jpg',
        'descricao': 'Máquinas envasadoras da linha TC 4S-3',
        'pagina': 'maquina-tc4s-3',
        'acessorios': []
    },

    'TC 3SC PÓ E SÓLIDOS': {
        'linha': 'Linha TC 3SC',
        'nome': 'Linha 3SC Pó e sólidos',
        'embalagem': [3, 4],
        'produto': [4, 5, 6],
        'imagem': '../static/images/maquinas/tC3S_po_solidos-com-embalagem.jpg',
        'descricao': 'Máquinas envasadoras da linha TC3SC Pós e sólidos',
        'pagina': 'maquina-tc3scps',
        'acessorios': []
    },

    'TC 3SC LÍQUIDOS E SECOS': {
        'linha': 'Linha TC 3SC',
        'nome': 'Linha 3SC Líquidos e secos',
        'embalagem': [3, 4],
        'produto': [1, 2, 3, 4, 5, 6],
        'imagem': '../static/images/maquinas/tc-3SC_liquidos_secos-com-embalagem.jpg',
        'descricao': 'Máquinas envasadoras da linha TC3SC Líquidos e secos',
        'pagina': 'maquina-tc3scls',
        'acessorios': []
    },

    'TC 3SC STICK': {
        'linha': 'Linha TC 3SC',
        'nome': 'Linha TC 3SC Stick',
        'embalagem': [3, 4],
        'produto': [1, 2, 3, 4, 5, 6],
        'imagem': '../static/images/maquinas/tc-3SC-stick-com-embalagem.jpg',
        'descricao': 'Máquinas envasadoras da linha TC3SC Stick',
        'pagina': 'maquina-tc3s',
        'acessorios': []
    },

    'TC-3SL': {
        'linha': 'Linha TC-3SL',
        'nome': 'Linha TC-3SL',
        'embalagem': [3, 4],
        'produto': [1, 2, 3, 4, 5, 6],
        'imagem': '../static/images/maquinas/tc-3SL-com-embalagem.jpg',
        'descricao': 'Máquinas envasadoras da linha TC-3SL',
        'pagina': 'maquina-tc3sl',
        'acessorios': []
    },

    'FRASCOS LINEAR': {
        'linha': 'Linha de frascos',
        'nome': 'Linha de frascos linear',
        'embalagem': [5, 6],
        'produto': [1, 2, 3, 4, 5, 6],
        'imagem': '../static/images/maquinas/linha-frascos-1-com-embalagem.jpg',
        'descricao': 'Máquinas envasadoras da linha de frascos linear',
        'pagina': 'maquina-frascoln',
        'acessorios': [],
    },

    'FRASCOS TRIBLOCK': {
        'linha': 'Linha de frascos',
        'nome': 'Linha de frascos triblock',
        'embalagem': [5, 6],
        'produto': [1, 2, 3],
        'imagem': '../static/images/maquinas/linha-frascos-2-com-embalagem.jpg',
        'descricao': 'Máquinas envasadoras da linha de frascos triblock',
        'pagina': 'maquina-frascotr',
        'acessorios': []
    },

    'FRASCOS ROTATIVA': {
        'linha': 'Linha de frascos',
        'nome': 'Linha de frascos rotativa',
        'embalagem': [5, 6],
        'produto': [1, 2, 3],
        'imagem': '../static/images/maquinas/linha-frascos-3-com-embalagem.jpg',
        'descricao': 'Máquinas envasadoras da linha de frascos rotativa',
        'pagina': 'maquina-frascortv',
        'acessorios': []
    },

    'FRASCOS SPEED': {
        'linha': 'Linha de frascos',
        'nome': 'Linha de frascos rotativa speed',
        'embalagem': [5, 6],
        'produto': [1, 2, 3],
        'imagem': '../static/images/maquinas/linha-frascos-4-com-embalagem.jpg',
        'descricao': 'Máquinas envasadoras da linha de frascos rotativa speed',
        'pagina': 'maquina-frascorts',
        'acessorios': []
    },

    'POTES': {
        'linha': 'Linha de potes',
        'nome': 'Linha de potes',
        'embalagem': [8],
        'produto': [1, 2, 3, 4, 5, 6],
        'imagem': '../static/images/maquinas/linha-potes-com-embalagem.jpg',
        'descricao': 'Máquinas envasadoras da linha de potes',
        'pagina': 'maquina-potes',
        'acessorios': []
    },

    'TC 4BC': {
        'linha': 'Linha Stand-Up Pouch',
        'nome': 'Linha TC 4B',
        'embalagem': [2, 3],
        'produto': [1, 2, 3, 4, 5, 6],
        'imagem': '../static/images/maquinas/stand-up-pouch-1-com-embalagem.jpg',
        'descricao': 'Máquinas envasadoras da linha TC 4BC',
        'pagina': 'maquina-tc4bc',
        'acessorios': []
    },

    'POUCH': {
        'linha': 'Linha Stand-Up Pouch',
        'nome': 'Linha Pouch pronto',
        'embalagem': [2, 3],
        'produto': [1, 2, 3, 4, 5, 6],
        'imagem': '../static/images/maquinas/pouch-pronto-com-embalagem.jpg',
        'descricao': 'Máquinas envasadoras da linha pouch pronto',
        'pagina': 'maquina-pouch',
        'acessorios': []
    },

    'TC SUP': {
        'linha': 'Linha Stand-Up Pouch',
        'nome': 'Linha TC SUP',
        'embalagem': [2, 3],
        'produto': [1, 2],
        'imagem': '../static/images/maquinas/mini-pouch-com-embalagem.jpg',
        'descricao': 'Máquinas envasadoras da linha TC SUP',
        'pagina': 'maquina-tcsup',
        'acessorios': []
    },

    'TC 4U': {
        'linha': 'Linha TC 4U',
        'nome': 'Linha TC 4U',
        'embalagem': [7],
        'produto': [6],
        'imagem': '../static/images/maquinas/tc-4u-com-embalagem.jpg',
        'descricao': 'Máquinas enfardadeiras da linha TC 4U',
        'pagina': 'maquina-tc4u',
        'acessorios': []
    }, 

    'PTC': {
        'linha': 'Linha PTC',
        'nome': 'Linha PTC',
        'embalagem': [3, 4],
        'produto': [4, 5, 6],
        'imagem': '../static/images/maquinas/ptc-com-embalagem.jpg',
        'descricao': 'Máquinas embaladoras da linha PTC',
        'pagina': 'maquina-ptc',
        'acessorios': []
    },

    'TC 3SC BAG': {
        'linha': 'Linha TC 3SC BAG',
        'nome': 'Linha TC 3SC BAG',
        'embalagem': [3, 4],
        'produto': [1, 2],
        'imagem': '../static/images/maquinas/tc3SC-com-embalagem.jpg',
        'descricao': 'Máquinas envasadoras da linha TC 3SC BAG',
        'pagina': 'maquina-tc3scb',
        'acessorios': []
    },

    'FLOWPACK': {
        'linha': 'Linha Flowpack',
        'nome': 'Linha Flowpack',
        'embalagem': [3, 4],
        'produto': [6],
        'imagem': '../static/images/maquinas/flowpack-com-embalagem.jpg',
        'descricao': 'Máquinas envasadoras da linha flowpack',
        'pagina': 'maquina-flowpack',
        'acessorios': []
    },

    'BISNAGAS': {
        'linha': 'Linha bisnagas',
        'nome': 'Linha bisnagas',
        'embalagem': [6],
        'produto': [1, 2],
        'imagem': '../static/images/maquinas/linha-bisnagas-com-embalagem.jpg',
        'descricao': 'Máquinas envasadoras da linha bisnagas',
        'pagina': 'maquina-bisnaga',
        'acessorios': []
    },

    'CARTONADAS': {
        'linha': 'Linha cartonadas',
        'nome': 'Linha embalagens cartonadas',
        'embalagem': [1],
        'produto': [1, 2, 3, 4, 5, 6],
        'imagem': '../static/images/maquinas/linha-embalagem-cartonada-com-embalagem.jpg',
        'descricao': 'Máquinas envasadoras da linha cartonada',
        'pagina': 'maquina-cartonada',
        'acessorios': []
    },

    'GALOES': {
        'linha': 'Linha de galões',
        'nome': 'Linha de galões',
        'embalagem': [5],
        'produto': [1],
        'imagem': '../static/images/maquinas/linha-galoes-com-embalagem.jpg',
        'descricao': 'Máquinas da linha de galões',
        'pagina': 'maquina-galao',
        'acessorios': []
    },

    'PET': {
        'linha': 'Linha PET',
        'nome': 'Pet com túnel',
        'embalagem': [5],
        'produto': [6],
        'imagem': '../static/images/maquinas/pet-com-tunel-com-embalagem.jpg',
        'descricao': 'Máquinas envolvedoras da linha PET com túnel',
        'pagina': 'maquina-pet',
        'acessorios': []
    }
}