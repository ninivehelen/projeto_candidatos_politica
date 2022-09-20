import datetime
ano_atual = datetime.datetime.now()
date = ano_atual.date()

def valida_ano(data):
  lista = list(data)
  if (data != 'nan'):
    ano = int(data)
      #Verifica se o ano é negativo
    if ano <= 0:
      return False
      
      #Verifica se o ano é menor que 4 digitos
    elif len(lista)< 4 or len(lista)>4:
      return False
      
      #verifica se é ano bissexto 
    elif (ano% 4 == 0) and (ano % 100 != 0 or ano % 400 == 0):
      return True

  else:
     return True
     

if(__name__ == '__main__'):
   data = '-21'
   resu = valida_ano(data)
   if resu == False:
      print("invalido")
   else:
    if data != 'nan':
      ano = date.strftime("%Y")
      ano = int(ano)
      data = int(data)
      if (data > ano):
        print("ano maior que ano atual")
       
       
   
