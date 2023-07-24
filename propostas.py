import sqlite3

def create_table_proposta(app):
    with app.app_context():
        connection = sqlite3.connect('propostas.db')
        cursor = connection.cursor()
        cursor.execute('CREATE TABLE IF NOT EXISTS propostas (version TEXT, accessories TEXT)')
        connection.commit()
        connection.close()

def insert_proposta(app, version, accessories):
    with app.app_context():
        connection = sqlite3.connect('propostas.db')
        cursor = connection.cursor()
        cursor.execute('INSERT INTO propostas (version, accessories) VALUES (?, ?)', (version, accessories))
        connection.commit()
        connection.close()

def get_propostas(app):
    with app.app_context():
        connection = sqlite3.connect('propostas.db')
        cursor = connection.cursor()
        cursor.execute('SELECT version, accessories FROM propostas')
        propostas = cursor.fetchall()
        connection.close()
        return propostas

def close_connection(app):
    with app.app_context():
        pass
