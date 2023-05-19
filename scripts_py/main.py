import pandas as pd 
from criar_banco import  conexao_mysql
import os 
caminho = os.getcwd()

#Unir csv dos anos de 1994 até 2008 e de 2010 até 2022
def unir_arquivos(candidatos_goias_1994_2008,candidatos_goias_2010_2022):
    #codigo para unir o csv
    df_final_candidatos_goias = pd.concat([candidatos_goias_1994_2008,candidatos_goias_2010_2022])
    print("unindo csv")
    df_final_candidatos_goias.to_csv('candidatos_goias_1994_2022.csv', sep=';',encoding="utf-8",index=False)
    print("Arquivo [candidatos_goias_1994_2022.csv] salvo!")
    

if __name__ == "__main__":
    candidatos_goias_1994_2008 = pd.read_csv(f'{caminho}/scripts_py/candidatos_goias_1994_2008_limpo.csv',sep=';', encoding='UTF-8')
    candidatos_goias_2010_2022 = pd.read_csv(f'{caminho}/scripts_py/candidatos_goias_2010_2022_limpo.csv',sep=';', encoding='UTF-8')
    unir_arquivos(candidatos_goias_1994_2008,candidatos_goias_2010_2022)
    conexao_mysql()
   

