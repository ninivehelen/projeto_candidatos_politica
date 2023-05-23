from mysql.connector import Error
import mysql.connector as msql
from mysql.connector import Error
from flask import Flask, make_response, jsonify,request
import yaml
import os 
caminho = os.getcwd()

#Credenciais do banco 
with open(f'{caminho}\scripts_py\credencial_banco.yaml', 'r') as f:
     credencial_banco= yaml.load(f, Loader=yaml.FullLoader)

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

#Conexao com banco de dados
try:
  conn = msql.connect(host = credencial_banco['credenciais_banco']['host'], database = credencial_banco['credenciais_banco']['database'] , user = credencial_banco['credenciais_banco']['user'],  
                           password = credencial_banco['credenciais_banco']['password'])
  print("Conectado")
       
except Error as e:
    print("Erro na conexão com o banco de dados", e)

@app.route('/candidatos_goias', methods = ['GET'])
def get_candidatos_goias():
    my_cursor = conn.cursor()
    my_cursor.execute("SELECT *from dados_candidatos_goias")
    candidatos_goias = my_cursor.fetchall()
    candidatos = list()
    for candidato in candidatos_goias:
         candidatos.append(
             {
                 'ID':candidato[0],
                 'ANO_ELEICAO':candidato[1],
                 'CD_TIPO_ELEICAO':candidato[2],
                 'NR_TURNO':candidato[3],
                 'CD_ELEICAO':candidato[4],
                 'DS_ELEICAO':candidato[5],
                 'TP_ABRAGENCIA':candidato[6],
                 'SG_UF':candidato[7],
                 'SG_UE':candidato[8],
                 'NM_UE':candidato[9],
                 'NM_CANDIDATO':candidato[10],
                 'NM_URNA_CANDIDATO':candidato[11],
                 'CD_SITUACAO_CANDIDATO':candidato[12],
                 'DS_SITUACAO_CANDIDATO':candidato[13],
                 'SG_PARTIDO':candidato[14],
                 'NM_PARTIDO':candidato[15],
                 'DS_NACIONALIDADE':candidato[16],
                 'DT_NASCIMENTO':candidato[17],
                 'NR_IDADE_DATA_POSE':candidato[18],
                 'DS_GENERO':candidato[19],
                 'DS_GRAU_INSTRUCAO':candidato[20],
                 'DS_ESTADO_CIVIL':candidato[21],
                 'DS_COR_RACA':candidato[22],
                 'DS_DESPESAS_MAX_CAMAPANHA':candidato[23],
                 'DS_SIT_TOT_TURNO':candidato[24],
                 'ST_REELEICAO':candidato[25],
                 'DS_SITUACAO_CANDIDATO_URNA':candidato[26],
                 'ST_CANDIDATO_INSERIDO_URNA':candidato[27]
             }
         )
    return make_response(
        jsonify(
          mensagem = 'Candidatos_goias',
          dados = candidatos
        )
    )

@app.route('/candidatos_goias/eleicao/nome_candidato/<string:nome>', methods = ['GET'])
def candidatos_goias_nome_candidato(nome):
    my_cursor = conn.cursor()
    my_cursor.execute(f'SELECT *from dados_candidatos_goias where nm_candidato = {nome}')
    candidatos_goias = my_cursor.fetchall()
    candidatos = list()
    for candidato in candidatos_goias:
         candidatos.append(
             {
                 'ID':candidato[0],
                 'ANO_ELEICAO':candidato[1],
                 'CD_TIPO_ELEICAO':candidato[2],
                 'NR_TURNO':candidato[3],
                 'CD_ELEICAO':candidato[4],
                 'DS_ELEICAO':candidato[5],
                 'TP_ABRAGENCIA':candidato[6],
                 'SG_UF':candidato[7],
                 'SG_UE':candidato[8],
                 'NM_UE':candidato[9],
                 'NM_CANDIDATO':candidato[10],
                 'NM_URNA_CANDIDATO':candidato[11],
                 'CD_SITUACAO_CANDIDATO':candidato[12],
                 'DS_SITUACAO_CANDIDATO':candidato[13],
                 'SG_PARTIDO':candidato[14],
                 'NM_PARTIDO':candidato[15],
                 'DS_NACIONALIDADE':candidato[16],
                 'DT_NASCIMENTO':candidato[17],
                 'NR_IDADE_DATA_POSE':candidato[18],
                 'DS_GENERO':candidato[19],
                 'DS_GRAU_INSTRUCAO':candidato[20],
                 'DS_ESTADO_CIVIL':candidato[21],
                 'DS_COR_RACA':candidato[22],
                 'DS_DESPESAS_MAX_CAMAPANHA':candidato[23],
                 'DS_SIT_TOT_TURNO':candidato[24],
                 'ST_REELEICAO':candidato[25],
                 'DS_SITUACAO_CANDIDATO_URNA':candidato[26],
                 'ST_CANDIDATO_INSERIDO_URNA':candidato[27]
             }
         )
    return make_response(
        jsonify(
          mensagem = 'Candidatos_goias',
          dados = candidatos
        )
    )

@app.route('/candidatos_goias/eleicao/ano_eleicao/<int:ano>', methods = ['GET'])
def candidatos_goias_ano_eleicao(ano):
    my_cursor = conn.cursor()
    my_cursor.execute(f'SELECT *from dados_candidatos_goias where ano_eleicao={ano}')
    candidatos_goias = my_cursor.fetchall()
    candidatos = list()
    for candidato in candidatos_goias:
         candidatos.append(
             {
                 'ID':candidato[0],
                 'ANO_ELEICAO':candidato[1],
                 'CD_TIPO_ELEICAO':candidato[2],
                 'NR_TURNO':candidato[3],
                 'CD_ELEICAO':candidato[4],
                 'DS_ELEICAO':candidato[5],
                 'TP_ABRAGENCIA':candidato[6],
                 'SG_UF':candidato[7],
                 'SG_UE':candidato[8],
                 'NM_UE':candidato[9],
                 'NM_CANDIDATO':candidato[10],
                 'NM_URNA_CANDIDATO':candidato[11],
                 'CD_SITUACAO_CANDIDATO':candidato[12],
                 'DS_SITUACAO_CANDIDATO':candidato[13],
                 'SG_PARTIDO':candidato[14],
                 'NM_PARTIDO':candidato[15],
                 'DS_NACIONALIDADE':candidato[16],
                 'DT_NASCIMENTO':candidato[17],
                 'NR_IDADE_DATA_POSE':candidato[18],
                 'DS_GENERO':candidato[19],
                 'DS_GRAU_INSTRUCAO':candidato[20],
                 'DS_ESTADO_CIVIL':candidato[21],
                 'DS_COR_RACA':candidato[22],
                 'DS_DESPESAS_MAX_CAMAPANHA':candidato[23],
                 'DS_SIT_TOT_TURNO':candidato[24],
                 'ST_REELEICAO':candidato[25],
                 'DS_SITUACAO_CANDIDATO_URNA':candidato[26],
                 'ST_CANDIDATO_INSERIDO_URNA':candidato[27]
             }
         )
    return make_response(
        jsonify(
          mensagem = 'Candidatos_goias',
          dados = candidatos
        )
    )

@app.route('/candidatos_goias/eleicao/situacao_candidato/<string:situacao>', methods = ['GET'])
def candidatos_goias_situacao(situacao):
    my_cursor = conn.cursor()
    my_cursor.execute(f'SELECT *from dados_candidatos_goias where ds_sit_tot_turno = {situacao}')
    candidatos_goias = my_cursor.fetchall()
    candidatos = list()
    for candidato in candidatos_goias:
         candidatos.append(
             {
                 'ID':candidato[0],
                 'ANO_ELEICAO':candidato[1],
                 'CD_TIPO_ELEICAO':candidato[2],
                 'NR_TURNO':candidato[3],
                 'CD_ELEICAO':candidato[4],
                 'DS_ELEICAO':candidato[5],
                 'TP_ABRAGENCIA':candidato[6],
                 'SG_UF':candidato[7],
                 'SG_UE':candidato[8],
                 'NM_UE':candidato[9],
                 'NM_CANDIDATO':candidato[10],
                 'NM_URNA_CANDIDATO':candidato[11],
                 'CD_SITUACAO_CANDIDATO':candidato[12],
                 'DS_SITUACAO_CANDIDATO':candidato[13],
                 'SG_PARTIDO':candidato[14],
                 'NM_PARTIDO':candidato[15],
                 'DS_NACIONALIDADE':candidato[16],
                 'DT_NASCIMENTO':candidato[17],
                 'NR_IDADE_DATA_POSE':candidato[18],
                 'DS_GENERO':candidato[19],
                 'DS_GRAU_INSTRUCAO':candidato[20],
                 'DS_ESTADO_CIVIL':candidato[21],
                 'DS_COR_RACA':candidato[22],
                 'DS_DESPESAS_MAX_CAMAPANHA':candidato[23],
                 'DS_SIT_TOT_TURNO':candidato[24],
                 'ST_REELEICAO':candidato[25],
                 'DS_SITUACAO_CANDIDATO_URNA':candidato[26],
                 'ST_CANDIDATO_INSERIDO_URNA':candidato[27]
             }
         )
    return make_response(
        jsonify(
          mensagem = 'Candidatos_goias',
          dados = candidatos
        )
    )

@app.route('/candidatos_goias/eleicao/escolaridade_candidato/<string:escolaridade>', methods = ['GET'])
def candidatos_goias_escolaridade_candidato(escolaridade):
    my_cursor = conn.cursor()
    my_cursor.execute(f'SELECT *from dados_candidatos_goias where ds_grau_instrucao = {escolaridade}')
    candidatos_goias = my_cursor.fetchall()
    candidatos = list()
    for candidato in candidatos_goias:
         candidatos.append(
             {
                 'ID':candidato[0],
                 'ANO_ELEICAO':candidato[1],
                 'CD_TIPO_ELEICAO':candidato[2],
                 'NR_TURNO':candidato[3],
                 'CD_ELEICAO':candidato[4],
                 'DS_ELEICAO':candidato[5],
                 'TP_ABRAGENCIA':candidato[6],
                 'SG_UF':candidato[7],
                 'SG_UE':candidato[8],
                 'NM_UE':candidato[9],
                 'NM_CANDIDATO':candidato[10],
                 'NM_URNA_CANDIDATO':candidato[11],
                 'CD_SITUACAO_CANDIDATO':candidato[12],
                 'DS_SITUACAO_CANDIDATO':candidato[13],
                 'SG_PARTIDO':candidato[14],
                 'NM_PARTIDO':candidato[15],
                 'DS_NACIONALIDADE':candidato[16],
                 'DT_NASCIMENTO':candidato[17],
                 'NR_IDADE_DATA_POSE':candidato[18],
                 'DS_GENERO':candidato[19],
                 'DS_GRAU_INSTRUCAO':candidato[20],
                 'DS_ESTADO_CIVIL':candidato[21],
                 'DS_COR_RACA':candidato[22],
                 'DS_DESPESAS_MAX_CAMAPANHA':candidato[23],
                 'DS_SIT_TOT_TURNO':candidato[24],
                 'ST_REELEICAO':candidato[25],
                 'DS_SITUACAO_CANDIDATO_URNA':candidato[26],
                 'ST_CANDIDATO_INSERIDO_URNA':candidato[27]
             }
         )
    return make_response(
        jsonify(
          mensagem = 'Candidatos_goias',
          dados = candidatos
        )
    )

@app.route('/candidatos_goias/eleicao/sigla_partido_candidato/<string:sigla>', methods = ['GET'])
def candidatos_goias_partido_sigla_candidato(sigla):
    my_cursor = conn.cursor()
    my_cursor.execute(f'SELECT *from dados_candidatos_goias where sg_partido = {sigla}')
    candidatos_goias = my_cursor.fetchall()
    candidatos = list()
    for candidato in candidatos_goias:
         candidatos.append(
             {
                 'ID':candidato[0],
                 'ANO_ELEICAO':candidato[1],
                 'CD_TIPO_ELEICAO':candidato[2],
                 'NR_TURNO':candidato[3],
                 'CD_ELEICAO':candidato[4],
                 'DS_ELEICAO':candidato[5],
                 'TP_ABRAGENCIA':candidato[6],
                 'SG_UF':candidato[7],
                 'SG_UE':candidato[8],
                 'NM_UE':candidato[9],
                 'NM_CANDIDATO':candidato[10],
                 'NM_URNA_CANDIDATO':candidato[11],
                 'CD_SITUACAO_CANDIDATO':candidato[12],
                 'DS_SITUACAO_CANDIDATO':candidato[13],
                 'SG_PARTIDO':candidato[14],
                 'NM_PARTIDO':candidato[15],
                 'DS_NACIONALIDADE':candidato[16],
                 'DT_NASCIMENTO':candidato[17],
                 'NR_IDADE_DATA_POSE':candidato[18],
                 'DS_GENERO':candidato[19],
                 'DS_GRAU_INSTRUCAO':candidato[20],
                 'DS_ESTADO_CIVIL':candidato[21],
                 'DS_COR_RACA':candidato[22],
                 'DS_DESPESAS_MAX_CAMAPANHA':candidato[23],
                 'DS_SIT_TOT_TURNO':candidato[24],
                 'ST_REELEICAO':candidato[25],
                 'DS_SITUACAO_CANDIDATO_URNA':candidato[26],
                 'ST_CANDIDATO_INSERIDO_URNA':candidato[27]
             }
         )
    return make_response(
        jsonify(
          mensagem = 'Candidatos_goias',
          dados = candidatos
        )
    )

@app.route('/candidatos_goias/eleicao/genero_candidato/<string:genero>', methods = ['GET'])
def candidatos_goias_genero_candidato(genero):
    my_cursor = conn.cursor()
    my_cursor.execute(f'SELECT *from dados_candidatos_goias where ds_genero = {genero}')
    candidatos_goias = my_cursor.fetchall()
    candidatos = list()
    for candidato in candidatos_goias:
         candidatos.append(
             {
                 'ID':candidato[0],
                 'ANO_ELEICAO':candidato[1],
                 'CD_TIPO_ELEICAO':candidato[2],
                 'NR_TURNO':candidato[3],
                 'CD_ELEICAO':candidato[4],
                 'DS_ELEICAO':candidato[5],
                 'TP_ABRAGENCIA':candidato[6],
                 'SG_UF':candidato[7],
                 'SG_UE':candidato[8],
                 'NM_UE':candidato[9],
                 'NM_CANDIDATO':candidato[10],
                 'NM_URNA_CANDIDATO':candidato[11],
                 'CD_SITUACAO_CANDIDATO':candidato[12],
                 'DS_SITUACAO_CANDIDATO':candidato[13],
                 'SG_PARTIDO':candidato[14],
                 'NM_PARTIDO':candidato[15],
                 'DS_NACIONALIDADE':candidato[16],
                 'DT_NASCIMENTO':candidato[17],
                 'NR_IDADE_DATA_POSE':candidato[18],
                 'DS_GENERO':candidato[19],
                 'DS_GRAU_INSTRUCAO':candidato[20],
                 'DS_ESTADO_CIVIL':candidato[21],
                 'DS_COR_RACA':candidato[22],
                 'DS_DESPESAS_MAX_CAMAPANHA':candidato[23],
                 'DS_SIT_TOT_TURNO':candidato[24],
                 'ST_REELEICAO':candidato[25],
                 'DS_SITUACAO_CANDIDATO_URNA':candidato[26],
                 'ST_CANDIDATO_INSERIDO_URNA':candidato[27]
             }
         )
    return make_response(
        jsonify(
          mensagem = 'Candidatos_goias',
          dados = candidatos
        )
    )

@app.route('/candidatos_goias/eleicao/raca_candidato/<string:raca>', methods = ['GET'])
def candidatos_goias_raca_candidato(raca):
    my_cursor = conn.cursor()
    my_cursor.execute(f'SELECT *from dados_candidatos_goias where ds_cor_raca = {raca}')
    candidatos_goias = my_cursor.fetchall()
    candidatos = list()
    for candidato in candidatos_goias:
         candidatos.append(
             {
                 'ID':candidato[0],
                 'ANO_ELEICAO':candidato[1],
                 'CD_TIPO_ELEICAO':candidato[2],
                 'NR_TURNO':candidato[3],
                 'CD_ELEICAO':candidato[4],
                 'DS_ELEICAO':candidato[5],
                 'TP_ABRAGENCIA':candidato[6],
                 'SG_UF':candidato[7],
                 'SG_UE':candidato[8],
                 'NM_UE':candidato[9],
                 'NM_CANDIDATO':candidato[10],
                 'NM_URNA_CANDIDATO':candidato[11],
                 'CD_SITUACAO_CANDIDATO':candidato[12],
                 'DS_SITUACAO_CANDIDATO':candidato[13],
                 'SG_PARTIDO':candidato[14],
                 'NM_PARTIDO':candidato[15],
                 'DS_NACIONALIDADE':candidato[16],
                 'DT_NASCIMENTO':candidato[17],
                 'NR_IDADE_DATA_POSE':candidato[18],
                 'DS_GENERO':candidato[19],
                 'DS_GRAU_INSTRUCAO':candidato[20],
                 'DS_ESTADO_CIVIL':candidato[21],
                 'DS_COR_RACA':candidato[22],
                 'DS_DESPESAS_MAX_CAMAPANHA':candidato[23],
                 'DS_SIT_TOT_TURNO':candidato[24],
                 'ST_REELEICAO':candidato[25],
                 'DS_SITUACAO_CANDIDATO_URNA':candidato[26],
                 'ST_CANDIDATO_INSERIDO_URNA':candidato[27]
             }
         )
    return make_response(
        jsonify(
          mensagem = 'Candidatos_goias',
          dados = candidatos
        )
    )

@app.route('/candidatos_goias/ano_situacao_raca_gerero_escolaridade/<int:ano>,<string:situacao>,<string:raca>,<string:genero>,<string:escolaridade>', methods = ['GET'])
def candidatos_goias_pesquisa_especifica(ano, situacao, raca, genero, escolaridade ):
    my_cursor = conn.cursor()
    my_cursor.execute(f'SELECT *from dados_candidatos_goias  where ano_eleicao ={ano} and ds_sit_tot_turno = {situacao} and ds_cor_raca = {raca} and ds_genero = {genero} and ds_grau_instrucao = {escolaridade}')
    candidatos_goias = my_cursor.fetchall()
    candidatos = list()
    for candidato in candidatos_goias:
         candidatos.append(
             {
                 'ID':candidato[0],
                 'ANO_ELEICAO':candidato[1],
                 'CD_TIPO_ELEICAO':candidato[2],
                 'NR_TURNO':candidato[3],
                 'CD_ELEICAO':candidato[4],
                 'DS_ELEICAO':candidato[5],
                 'TP_ABRAGENCIA':candidato[6],
                 'SG_UF':candidato[7],
                 'SG_UE':candidato[8],
                 'NM_UE':candidato[9],
                 'NM_CANDIDATO':candidato[10],
                 'NM_URNA_CANDIDATO':candidato[11],
                 'CD_SITUACAO_CANDIDATO':candidato[12],
                 'DS_SITUACAO_CANDIDATO':candidato[13],
                 'SG_PARTIDO':candidato[14],
                 'NM_PARTIDO':candidato[15],
                 'DS_NACIONALIDADE':candidato[16],
                 'DT_NASCIMENTO':candidato[17],
                 'NR_IDADE_DATA_POSE':candidato[18],
                 'DS_GENERO':candidato[19],
                 'DS_GRAU_INSTRUCAO':candidato[20],
                 'DS_ESTADO_CIVIL':candidato[21],
                 'DS_COR_RACA':candidato[22],
                 'DS_DESPESAS_MAX_CAMAPANHA':candidato[23],
                 'DS_SIT_TOT_TURNO':candidato[24],
                 'ST_REELEICAO':candidato[25],
                 'DS_SITUACAO_CANDIDATO_URNA':candidato[26],
                 'ST_CANDIDATO_INSERIDO_URNA':candidato[27]
             }
         )
    return make_response(
        jsonify(
          mensagem = 'Candidatos_goias',
          dados = candidatos
        )
    )


@app.route('/candidatos_goias/eleicao/regiao/<string:regiao>', methods = ['GET'])
def candidatos_goias_raca_candidato(regiao):
    my_cursor = conn.cursor()
    my_cursor.execute(f'SELECT *from dados_candidatos_goias where NM_UE = {regiao}')
    candidatos_goias = my_cursor.fetchall()
    candidatos = list()
    for candidato in candidatos_goias:
         candidatos.append(
             {
                 'ID':candidato[0],
                 'ANO_ELEICAO':candidato[1],
                 'CD_TIPO_ELEICAO':candidato[2],
                 'NR_TURNO':candidato[3],
                 'CD_ELEICAO':candidato[4],
                 'DS_ELEICAO':candidato[5],
                 'TP_ABRAGENCIA':candidato[6],
                 'SG_UF':candidato[7],
                 'SG_UE':candidato[8],
                 'NM_UE':candidato[9],
                 'NM_CANDIDATO':candidato[10],
                 'NM_URNA_CANDIDATO':candidato[11],
                 'CD_SITUACAO_CANDIDATO':candidato[12],
                 'DS_SITUACAO_CANDIDATO':candidato[13],
                 'SG_PARTIDO':candidato[14],
                 'NM_PARTIDO':candidato[15],
                 'DS_NACIONALIDADE':candidato[16],
                 'DT_NASCIMENTO':candidato[17],
                 'NR_IDADE_DATA_POSE':candidato[18],
                 'DS_GENERO':candidato[19],
                 'DS_GRAU_INSTRUCAO':candidato[20],
                 'DS_ESTADO_CIVIL':candidato[21],
                 'DS_COR_RACA':candidato[22],
                 'DS_DESPESAS_MAX_CAMAPANHA':candidato[23],
                 'DS_SIT_TOT_TURNO':candidato[24],
                 'ST_REELEICAO':candidato[25],
                 'DS_SITUACAO_CANDIDATO_URNA':candidato[26],
                 'ST_CANDIDATO_INSERIDO_URNA':candidato[27]
             }
         )
    return make_response(
        jsonify(
          mensagem = 'Candidatos_goias',
          dados = candidatos
        )
    )
app.run()