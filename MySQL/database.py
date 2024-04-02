import mysql.connector
from mysql.connector import Error
import pandas as pd

def create_server_connection(host_name, user_name, host_password, db_name=None, *args, **kwargs):
    connection = None

    try:
        connection = mysql.connector.connect(host=host_name, user=user_name, passwd=host_password, database=db_name)
        print('Conexão realizada com sucesso!')
    
    except Error as err:
        print(f'Erro: {err}')

    return connection

def querry_entrada(conexao, querry):
    cursor = conexao.cursor()

    try:
        cursor.execute(querry)
        conexao.commit()
        print(f'{querry} realizada com suceso')
    except Error as err:
        print(f'Erro: {err}')

conexao = create_server_connection('LocalHost', 'root', 'Mysql64207@', 'ifce')

# CREATE TABLE aluno_faculdade(id_aluno INT NOT NULL AUTO_INCREMENT, nome VARCHAR(40) NOT NULL, 
#semestre INT NOT NULL, data_nascimento DATE, sexo ENUM('M', 'F'), PRIMARY KEY(id_aluno));


def insert_novo_aluno_faculdade(nome, semestre, data_nascimento, sexo, *args, **kwargs):
     execute = querry_entrada(conexao, f"INSERT INTO aluno_faculdade(nome, semestre, data_nascimento, sexo) VALUES ('{nome}', '{semestre}', '{data_nascimento}', '{sexo}');")
     return execute

insert_novo_aluno_faculdade("Marcos antônio", 4, "2001-10-25", "M")