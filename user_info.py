import mysql.connector

def create_table_user(app):
    with app.app_context():
        connection = mysql.connector.connect(
            host='mysql.profills.com',
            user='profills03',
            # password= ''
            database='profills03'
        )
        cursor = connection.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS user_info (
                          id INT AUTO_INCREMENT PRIMARY KEY,
                          nome VARCHAR(255),
                          endereco VARCHAR(255),
                          celular VARCHAR(255),
                          email VARCHAR(255),
                          empresa VARCHAR(255),
                          cnpj VARCHAR(255),
                          cep VARCHAR(255),
                          numero VARCHAR(255),
                          cidade VARCHAR(255),
                          estado VARCHAR(255),
                          pais VARCHAR(255)
                          )''')
        connection.commit()
        connection.close()

def insert_info(app, nome, endereco, celular, email, empresa, cnpj, cep, cidade, estado, pais):
    with app.app_context():
        connection = mysql.connector.connect(
            host='mysql.profills.com',
            user='profills03',
            # password='',
            database='profills03'
        )
        cursor = connection.cursor()
        cursor.execute('''INSERT INTO user_info (nome, endereco, celular, email, empresa, cnpj, cep, cidade, estado, pais)
                          VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)''',
                       (nome, endereco, celular, email, empresa, cnpj, cep, cidade, estado, pais))
        connection.commit()
        connection.close()

def get_info(app):
    with app.app_context():
        connection = mysql.connector.connect(
            host='mysql.profills.com',
            user='profills03',
            # password= ''
            database='profills03'
        )
        cursor = connection.cursor()
        cursor.execute('''SELECT nome, endereco, celular, email, empresa, cnpj, cep, cidade, estado, pais FROM user_info''')
        user_info = cursor.fetchall()
        connection.close()
        return user_info

def close_connection(app):
    with app.app_context():
        pass