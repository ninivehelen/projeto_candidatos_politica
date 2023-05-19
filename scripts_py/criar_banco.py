import pandas as pd 
import mysql.connector as msql
from mysql.connector import Error
from salvar_dados import conexao_banco
import yaml
import os 

caminho = os.getcwd()


#credencias banco de dados 
with open(f'{caminho}\scripts_py\credencial_banco.yaml', 'r') as f:
     credencial_banco= yaml.load(f, Loader=yaml.FullLoader)


def conexao_mysql():
    try:
        conn = msql.connect(host = credencial_banco['credenciais_banco']['host'], user = credencial_banco['credenciais_banco']['user'],  
                           password = credencial_banco['credenciais_banco']['password'])
        print("Conexão realizada com sucesso!")
    except Error as e:
       print("Erro na conexão", e)
    cria_banco_dados(conn) 
    

def cria_banco_dados(conn):
    try:
        if conn.is_connected():
                cursor = conn.cursor()
                cursor.execute('DROP DATABASE IF EXISTS candidatos_goias;')
                cursor.execute("CREATE DATABASE candidatos_goias")
                print("Banco de dados criado!")  
    except Error as e:
       print("Banco de dados não foi criado", e)
    conexao_banco()
   