import sqlite3
import uuid


def create_table_user(app):
    with app.app_context():
        connection = sqlite3.connect('user_info.db')
        cursor = connection.cursor()
        cursor.execute(
            'CREATE TABLE IF NOT EXISTS user_info (id TEXT PRIMARY KEY, nome TEXT, endereco TEXT, celular TEXT, email TEXT, empresa TEXT, cnpj TEXT)')

        connection.commit()
        connection.close()


def insert_info(app, user_id, nome, endereco, celular, email, empresa, cnpj):
    with app.app_context():
        connection = sqlite3.connect('user_info.db')
        cursor = connection.cursor()
        cursor.execute('INSERT INTO user_info (id, nome, endereco, celular, email, empresa, cnpj) VALUES (?, ?, ?, ?, ?, ?, ?)',
                       (user_id, nome, endereco, celular, email, empresa, cnpj))
        connection.commit()
        connection.close()


def get_info(app):
    with app.app_context():
        connection = sqlite3.connect('user_info.db')
        cursor = connection.cursor()
        cursor.execute(
            'SELECT nome, endereco, celular, email, empresa, cnpj FROM user_info')
        user_info = cursor.fetchall()
        connection.close()
        return user_info


def close_connection(app):
    with app.app_context():
        pass
