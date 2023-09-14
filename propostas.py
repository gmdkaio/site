import sqlite3

def create_table_proposta(app):
    with app.app_context():
        connection = sqlite3.connect('propostas.db')
        cursor = connection.cursor()
        cursor.execute('CREATE TABLE IF NOT EXISTS propostas (user_id TEXT, versao TEXT, accessorios TEXT, produtos TEXT, embalagens TEXT, data TEXT, descricao TEXT, peso TEXT, unidade_peso TEXT)')
        connection.commit()
        connection.close()

def insert_proposta(app, user_id, versao, accessorios, produtos, embalagens, data, descricao, peso, unidade_peso):
    with app.app_context():
        connection = sqlite3.connect('propostas.db')
        cursor = connection.cursor()
        cursor.execute('INSERT INTO propostas (user_id, versao, accessorios, produtos, embalagens, data, descricao, peso, unidade_peso) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)', (user_id, versao, accessorios, produtos, embalagens, data, descricao, peso, unidade_peso))
        connection.commit()
        connection.close()

def get_propostas(app):
    with app.app_context():
        connection = sqlite3.connect('propostas.db')
        cursor = connection.cursor()
        cursor.execute('SELECT versao, acessorios, produtos, embalagens, data, descricao, peso, unidade_peso FROM propostas')
        propostas = cursor.fetchall()
        connection.close()
        return propostas

def close_connection(app):
    with app.app_context():
        pass
