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

Maquinas = {
    'TP': {
        'linha': 'Linha TP',
        'linha_texto': 'A Linha TP de maquinas envasadoras para sache oferece envase preciso e rápido para uma variedade de produtos, de líquidos a secos, garantindo embalagens de alta qualidade, com ótimo selamento.',
        'nome': 'Linha TP',
        "variacao": 'variam de acordo com o tamanho da embalagem',
        'embalagem': [3, 4],
        'modelos': ['TP 85', 'TP 100', 'TP 120', 'TP 140', 'TP 180', 'TP 300'],
        'produto': [1, 2, 3, 4, 5, 6],
        'imagem': '../static/images/maquinas/tp-com-embalagem.jpg',
        'imagem_pag_maquina': '/static/images/maquinas/tp.png',
        'descricao': 'Máquinas envasadoras para sache 2 soldas, linha TP 80 a 340',
        'pagina': 'maquina-tp',
        'acessorios': [],
        'espessura_filme': ' 60 a 90 [μm]',
        'material_embalagem': 'PEBD e PEAD',
        'produto_texto': 'Liquidos e Secos',
        'info_tecnicas': {
            'producao': '3.000',
            'datador': 'Hotstamping',
            'dosagem': 'Temporizado | Bomba Positiva | Volumétrico',
            'tensao': '220 [V] - 60 [Hz]',
            'potencia_instalada': '1,95 a 2,15',
            'potencia_consumida': '1,20 a 1,80',
            'comando': 'CLP com IHM Touchscreen',
            'consumo_ar': '277[L/min]',
            'area': '2,1x2,45',
            'material': 'Aço inoxidável AISI 304, alumínio, policarbonato e aço carbono'
        },
        'info_embalagem': {
            'variacao': 'A altura dos saches pode ser personalizada',
            'TP85': {
                'largura': '85',
                'final': '35',
            },
            'TP100': {
                'largura': '100',
                'final': '45',
            },
            'TP120': {
                'largura': '120',
                'final': '55',
            },
            'TP140': {
                'largura': '140',
                'final': '65',
            },
            'TP180': {
                'largura': '180',
                'final': '80',
            },
            'TP300': {
                'largura': '85',
                'final': '140',
            },
        }
    },

    'TC 4S-1': {
        'linha': 'Linha TC 4S',
        'linha_texto': 'A Linha TC4S de maquinas envasadoras para sache oferece envase preciso e rápido para uma variedade de produtos, de líquidos a secos, garantindo embalagens de alta qualidade, com ótimo selamento.',
        'nome': 'Linha TP',
        "variacao": 'variam de acordo com o tamanho da embalagem',
        'embalagem': [3, 4],
        'modelos': ['TC 4S 120-1', 'TC 42 200-1', 'TC 4S 300-1', 'TC 4S 360-1', 'TC 4S-1 FORMATO ESPECIAL'],
        'produto': [1, 2, 3, 4, 5, 6],
        'imagem': '../static/images/maquinas/tc4S-1-com-embalagem.jpg',
        'imagem_pag_maquina': '/static/images/maquinas/tc4S-1.jpg',
        'descricao': 'Máquinas envasadoras para sache 4 soldas, linha TC 4S-1 120 a 360, além do formato especial',
        'pagina': 'maquina-tc4s-1',
        'acessorios': [],
        'espessura_filme': 'e 40 a 100 [μm',
        'material_embalagem': 'PET + PE | PET + PE + Al | BOPP | BOPPA | EVOH',
        'produto_texto': 'Líquidos e secos',
        'info_tecnicas': {
            'producao': '2.000',
            'datador': 'Alto relevo, inkjet ou hotstamping',
            'dosagem': 'Temporizado | Bomba positiva | Volumétrico',
            'tensao': '220 [V] - 60 [Hz]',
            'potencia_instalada': '2,37 [kW]',
            'potencia_consumida': '2,05 [kW.h]',
            'comando': 'CLP com IHM Touchscreen',
            'consumo_ar': '360 [L/min]',
            'area': '2.250x2.400 [mm²]',
            'material': 'Aço inoxidável AISI 304, alumínio, policarbonato e aço carbono'
        },
        'info_embalagem': {
            'variacao': 'A altura dos saches pode ser personalizada',
            'TC 4S 120-1': {
                'largura': '120',
                'final': '50',
            },
            'TC 4S 200-1': {
                'largura': '200',
                'final': '90',
            },
            'TC 4S 300-1': {
                'largura': '300',
                'final': '140',
            },
            'TC 4S 360-1': {
                'largura': '360',
                'final': '170',
            },
            'TC 4S-1 FORMATO ESPECIAL': {
                'largura': '360',
                'final': '170',
            },
        },
    },

    'TC 4S-2': {
        'linha': 'Linha TC 4S',
        'linha_texto': 'A Linha TC4S de maquinas envasadoras para sache oferece envase preciso e rápido para uma variedade de produtos, de líquidos a secos, garantindo embalagens de alta qualidade, com ótimo selamento.',
        'nome': 'Linha TC 4S-2',
        "variacao": 'variam de acordo com o tamanho da embalagem',
        'embalagem': [3, 4],
        'modelos': ['TC 4S 200-2', 'TC 4S 240-2', 'TC 4S 280-2', 'TC 4S 360-2', 'TC 4S-2 FORMATO ESPECIAL'],
        'produto': [1, 2, 3, 4, 5, 6],
        'imagem': '../static/images/maquinas/tc4S-2-com-embalagem.jpg',
        'imagem_pag_maquina': '/static/images/maquinas/tc4S-2.jpg',
        'descricao': 'Máquinas envasadoras para sache 4 soldas, linha TC 4S-2 200 a 360, além do formato especial',
        'pagina': 'maquina-tc4s-2',
        'acessorios': [],
        'espessura_filme': '50 a 100 [μm]',
        'material_embalagem': 'PET + PE | PET + PE + Al | BOPP | BOPPA | EVOH',
        'produto_texto': 'Líquidos e secos',
        'info_tecnicas': {
            'producao': '4.000',
            'datador': 'Alto relevo, hotstamping ou inkjet',
            'dosagem': 'Temporizado | Bomba positiva | Volumétrico',
            'tensao': '220 [V] - 60 [Hz]',
            'potencia_instalada': '2,75 [kW]',
            'potencia_consumida': '2,40 [kW.h]',
            'comando': 'CLP com IHM Touchscreen',
            'consumo_ar': '360 [L/min]',
            'area': '2.250x2.400 [mm²]',
            'material': 'Aço inoxidável AISI 304, alumínio, policarbonato e aço carbono'
        },
        'info_embalagem': {
            'variacao': 'A altura dos saches pode ser personalizada',
            'TC 4S 200-2': {
                'largura': '200',
                'final': '90',
            },
            'TC 4S 240-2': {
                'largura': '240',
                'final': '110',
            },
            'TC 4S 280-2': {
                'largura': '280',
                'final': '130',
            },
            'TC 4S 360-2': {
                'largura': '360',
                'final': '170',
            },
            'TC 4S-2 FORMATO ESPECIAL': {
                'largura': '360',
                'final': '170',
            },
        }
    },

    'TC 4S-3': {
        'linha': 'Linha TC 4S',
        'linha_texto': 'A Linha TC4S de maquinas envasadoras para sache oferece envase preciso e rápido para uma variedade de produtos, de líquidos a secos, garantindo embalagens de alta qualidade, com ótimo selamento.',
        'nome': 'Linha TC 4S-3',
        "variacao": 'variam de acordo com o tamanho da embalagem',
        'embalagem': [3, 4],
        'modelos': ['TC 4S 200-3', 'TC 4S 300-3', 'TC 4S 400-3', 'TC 4S-3 FORMATO ESPECIAL'],
        'produto': [1, 2, 3, 4, 5, 6],
        'imagem': '../static/images/maquinas/tc4S-3-com-embalagem.jpg',
        'imagem_pag_maquina': '/static/images/maquinas/tc4S-3.jpg',
        'descricao': 'Máquinas envasadoras para sache 4 soldas, linha TC 4S-3 200 a 400, além do formato especial',
        'pagina': 'maquina-tc4s-3',
        'acessorios': [],
        'espessura_filme': '50 a 100 [μm]',
        'material_embalagem': 'PET + PE | PET + PE + Al | BOPP | BOPPA | EVOH',
        'produto_texto': 'Líquidos e secos',
        'info_tecnicas': {
            'producao': '6.000',
            'datador': 'Alto relevo, hotstamping ou inkjet',
            'dosagem': 'Temporizado | Bomba positiva | Volumétrico',
            'tensao': '220 [V] - 60 [Hz]',
            'potencia_instalada': '3,19 a 3,43 [kW]',
            'potencia_consumida': '2,75 a 3,05 [kW.h]',
            'comando': 'CLP com IHM Touchscreen',
            'consumo_ar': '360 [L/min]',
            'area': '2.250x2.400 [mm²]',
            'material': 'Aço inoxidável AISI 304, alumínio, policarbonato e aço carbono'
        },
        'info_embalagem': {
            'variacao': 'A altura dos saches pode ser personalizada',
            'TC 4S 200-3': {
                'largura': '200',
                'final': '90',
            },
            'TC 4S 300-3': {
                'largura': '300',
                'final': '140',
            },
            'TC 4S 400-3': {
                'largura': '400',
                'final': '190',
            },
            'TC 4S-2 FORMATO ESPECIAL': {
                'largura': '400',
                'final': '190',
            },
        }
    },

    'TC 3SC PÓ E SÓLIDOS': {
        'linha': 'Linha TC 3SC',
        'linha_texto': 'A Linha TC 3SC de maquinas envasadoras para sache 3 soldas  oferece envase preciso e rápido para uma variedade de produtos, de líquidos a secos, garantindo embalagens de alta qualidade, com ótimo selamento.',
        'nome': 'Linha TC 3SC Pó e sólidos',
        "variacao": 'variam de acordo com o tamanho da embalagem',
        'embalagem': [3, 4],
        'modelos': ['TC 3SC 100-1', 'TC 3SC 200-1', 'TC 3SC 240-1', 'TC 3SC 360-1', 'TC 3SC FORMATO ESPECIAL'],
        'produto': [4, 5, 6],
        'imagem': '../static/images/maquinas/tC3S_po_solidos-com-embalagem.jpg',
        'imagem_pag_maquina': '/static/images/maquinas/tC3S_po_solidos.jpg',
        'descricao': 'Máquinas envasadoras da linha TC3SC Pós e sólidos',
        'pagina': 'maquina-tc3scps',
        'acessorios': [],
        'espessura_filme': '50 a 100 [µm]',
        'material_embalagem': 'PET + PE | PET + PE + Al | BOPP | BOPPA | EVOH',
        'produto_texto': 'Pós e sólidos',
        'info_tecnicas': {
            'producao': '1.800',
            'datador': 'Alto relevo, hotstamping ou inkjet',
            'dosagem': 'Temporizado ou Volumétrico',
            'tensao': '220 [V] - 60 [Hz]',
            'potencia_instalada': '1,97 [kW]',
            'potencia_consumida': '1,80 [kW.h]',
            'comando': 'CLP com IHM Touchscreen',
            'consumo_ar': '245 [L/min]',
            'area': '2.300x2.600 [mm²]',
            'material': 'Aço inoxidável AISI 304, alumínio, policarbonato e aço carbono'
        },
        'info_embalagem': {
            'variacao': 'A altura dos saches pode ser personalizada',
            'TC 3SC 100-1': {
                'largura': '100',
                'final': '40',
            },
            'TC 3SC 200-1': {
                'largura': '200',
                'final': '90',
            },
            'TC 3SC 240-1': {
                'largura': '240',
                'final': '110',
            },
            'TC 3SC 360-1': {
                'largura': '360',
                'final': '170',
            },
            'TC 3SC FORMATO ESPECIAL': {
                'largura': '360',
                'final': '170',
            },
        }
    },

    'TC 3SC LÍQUIDOS E SECOS': {
        'linha': 'Linha 3SC',
        'linha_texto': 'A Linha TC 3SC de maquinas envasadoras para sache 3 soldas  oferece envase preciso e rápido para uma variedade de produtos, de líquidos a secos, garantindo embalagens de alta qualidade, com ótimo selamento.',
        'nome': 'Linha TC 3SC Líquidos e secos',
        "variacao": 'variam de acordo com o tamanho da embalagem',
        'embalagem': [3, 4],
        'modelos': ['TC 3SC 100-1', 'TC 3SC 200-1', 'TC 3SC 350-1', 'TC 3SC FORMATO ESPECIAL'],
        'produto': [1, 2, 3, 4, 5, 6],
        'imagem': '../static/images/maquinas/tc-3SC_liquidos_secos-com-embalagem.jpg',
        'imagem_pag_maquina': '/static/images/maquinas/tc-3SC_liquidos_secos.jpg',
        'descricao': 'Máquinas envasadoras da linha TC3SC Líquidos e secos',
        'pagina': 'maquina-tc3scls',
        'acessorios': [],
        'espessura_filme': '',
        'material_embalagem': '',
        'produto_texto': '',
        'info_tecnicas': {
            'producao': '',
            'datador': '',
            'dosagem': '',
            'tensao': '',
            'potencia_instalada': '',
            'potencia_consumida': '',
            'comando': '',
            'consumo_ar': '',
            'area': '',
            'material': ''
        },
        'info_embalagem': {
            'variacao': '',
            '': {
                'largura': '',
                'final': '',
            },
            '': {
                'largura': '',
                'final': '',
            },
            '': {
                'largura': '',
                'final': '',
            },
            '': {
                'largura': '',
                'final': '',
            },
            '': {
                'largura': '',
                'final': '',
            },
            '': {
                'largura': '',
                'final': '',
            },
        }
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
