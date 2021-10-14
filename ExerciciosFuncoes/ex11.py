#Construa uma função que receba uma data no formato DD/MM/AAAA e devolva uma string no formato D de mesPorExtenso de AAAA. Opcionalmente, 
# valide a data e retorne NULL caso a data seja inválida.

mes = ['Janeiro','Fevereiro','Março','Abril','Maio','Junho','Julho','Agosto','Setembro','Outubro','Novembro','Dezembro']

def data(data):
    print(data.split('/')[0], 'de',mes[(int(data.split("/")[1])-1)],"de",data.split("/")[2])


x = input("Digite um data 'dd/mm/aaaa': ")

data(x)


