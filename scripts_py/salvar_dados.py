from mysql.connector import Error
import mysql.connector as msql
from mysql.connector import Error
import pandas as pd
import yaml 
import os 
caminho = os.getcwd()

#credencias banco de dados 
with open(f'{caminho}\scripts_py\credencial_banco.yaml', 'r') as f:
     credencial_banco= yaml.load(f, Loader=yaml.FullLoader)

#abertura dos dados

def conexao_banco():
    try:
        conn = msql.connect(host = credencial_banco['credenciais_banco']['host'], database = credencial_banco['credenciais_banco']['database'] , user = credencial_banco['credenciais_banco']['user'],  
                           password = credencial_banco['credenciais_banco']['password'])
        salvar_dados_banco(conn)
    except Error as e:
       print("Erro na conexão com o banco de dados", e)
    
def salvar_dados_banco(conn):
 dados_candidatos = pd.read_csv(f'{caminho}/candidatos_goias_1994_2022.csv', index_col=False, delimiter = ';')
 print("Dados carregados")
 try:
    if conn.is_connected():
        cursor = conn.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("Você esta conectado ao banco de dados: ", record)
        cursor.execute('DROP TABLE IF EXISTS candidatos_goias;')
        print('Criando Tabela')
# in the below line please pass the create table statement which you want #to create
        cursor.execute("CREATE TABLE dados_candidatos_goias(id int(2),ano_eleicao varchar(200),cd_tipo_eleicao varchar(255),nr_turno int (3),cd_eleicao varchar(200), ds_eleicao varchar(200), tp_abregencia varchar(200),sg_uf varchar(200),sg_ue varchar(200),nm_ue varchar(255),nm_candidato varchar(255),nm_urna_candidato varchar(255),cd_situacao_candidatura int(3),ds_situacao_candidato varchar(200), sg_partido varchar(200), nm_partido varchar(200), ds_nacionalidade varchar(200), dt_nascimento varchar(200), nr_idade_data_pose int(20), ds_genero varchar(200), ds_grau_instrucao varchar(200), ds_estado_civil varchar(200),ds_cor_raca varchar(200), ds_despesas_max_camapanha varchar(200), ds_sit_tot_turno varchar(200),st_releicao varchar(200), ds_situacao_candidato_urna varchar(200), st_candidato_inserido_urna varchar(200))")
        print("Tabela criada")
        #loop through the data frame
        for i,row in dados_candidatos.iterrows():
            #here %S means string values 
            sql = "INSERT INTO candidatos_goias.dados_candidatos_goias VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            cursor.execute(sql, tuple(row))
            print("Dado inserido")
            # the connection is not auto committed by default, so we must commit to save our changes
            conn.commit()
        print("Todos os dados inserido com sucesso !")
 except Error as e:
            print("Não conectado", e)