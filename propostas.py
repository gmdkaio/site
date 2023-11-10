import mysql.connector

def create_table_proposta(app):
    with app.app_context():
        connection = mysql.connector.connect(
            host='mysql.profills.com',
            user='profills02',
            # password=''
            database='profills02'
        )
        cursor = connection.cursor()
        cursor.execute('CREATE TABLE IF NOT EXISTS propostas (versao VARCHAR(255), accessorios TEXT, produtos TEXT, embalagens TEXT, data TEXT, descricao TEXT, peso TEXT, unidade_peso TEXT)')
        connection.commit()
        connection.close()

def insert_proposta(app, versao, accessorios, produtos, embalagens, data, descricao, peso, unidade_peso):
    with app.app_context():
        connection = mysql.connector.connect(
            host='mysql.profills.com',
            user='profills02',
            # password='',
            database='profills02'
        )
        cursor = connection.cursor()
        cursor.execute('INSERT INTO propostas (versao, accessorios, produtos, embalagens, data, descricao, peso, unidade_peso) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)', (versao, accessorios, produtos, embalagens, data, descricao, peso, unidade_peso))
        connection.commit()
        connection.close()

def get_propostas(app):
    with app.app_context():
        connection = mysql.connector.connect(
            host='mysql.profills.com',
            user='profills02',
            # password=''
            database='profills02'
        )
        cursor = connection.cursor()
        cursor.execute('SELECT versao, accessorios, produtos, embalagens, data, descricao, peso, unidade_peso FROM propostas')
        propostas = cursor.fetchall()
        connection.close()
        return propostas

def close_connection(app):
    with app.app_context():
        pass
