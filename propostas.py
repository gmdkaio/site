import sqlite3

def create_table_proposta(app):
    with app.app_context():
        connection = sqlite3.connect('propostas.db')
        cursor = connection.cursor()
        cursor.execute('CREATE TABLE IF NOT EXISTS propostas (user_id TEXT, versao TEXT, linha TEXT, accessorios TEXT, produtos TEXT, embalagens TEXT, data TEXT)')
        connection.commit()
        connection.close()

def insert_proposta(app, user_id, versao, linha, accessorios, produtos, embalagens, data):
    with app.app_context():
        connection = sqlite3.connect('propostas.db')
        cursor = connection.cursor()
        cursor.execute('INSERT INTO propostas (user_id, versao, linha, accessorios, produtos, embalagens, data) VALUES (?, ?, ?, ?, ?, ?, ?)', (user_id, versao, linha, accessorios, produtos, embalagens, data))
        connection.commit()
        connection.close()

def get_propostas(app):
    with app.app_context():
        connection = sqlite3.connect('propostas.db')
        cursor = connection.cursor()
        cursor.execute('SELECT versao, linha, acessorios, produtos, embalagens, data FROM propostas')
        propostas = cursor.fetchall()
        connection.close()
        return propostas

def close_connection(app):
    with app.app_context():
        pass
