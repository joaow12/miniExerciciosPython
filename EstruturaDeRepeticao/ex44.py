#Em uma eleição presidencial existem quatro candidatos. Os votos são informados por meio de código. Os códigos utilizados são:
#1 , 2, 3, 4  - Votos para os respectivos candidatos 
#(você deve montar a tabela ex: 1 - Jose/ 2- João/etc)
#5 - Voto Nulo
#6 - Voto em Branco
#Faça um programa que calcule e mostre:
#O total de votos para cada candidato;
#O total de votos nulos;
#O total de votos em branco;
#A percentagem de votos nulos sobre o total de votos;
#A percentagem de votos em branco sobre o total de votos. Para finalizar o conjunto de votos tem-se o valor zero.

candUm = 0
candDois = 0
candTres = 0
candQua = 0
nulo = 0
branco = 0
cod = True

while cod != 0:
    print('Para quem você deseja votar?')
    print('1 - José \n2 - João \n3 - Fulano \n4 - Siclano \n5 - Voto Nulo \n6 - Voto em Branco')
    cod = int(input("Digite em quem você deseja votar: "))
    if cod == 1:
        candUm += 1
    elif cod == 2:
        candDois += 1
    elif cod == 3:
        candTres += 1
    elif cod == 4:
        candQua += 1
    elif cod == 5:
        nulo += 1
    elif cod == 6:
        branco += 1

total = candUm+candDois+candTres+candQua+nulo+branco

print('TOTAL DE VOTOS: {0}'.format(total))
print('1 - José = {0} VOTOS \n2 - João = {1} VOTOS \n3 - Fulano = {2} VOTOS \n4 - Siclano = {3} VOTOS \n5 - Voto Nulo = {4} VOTOS \n6 - Voto em Branco = {5} VOTOS '.format(candUm, candDois, candTres, candQua, nulo, branco))
print('Porcentagem de votos nulos sobre o total de votos: {0} \nPorcentagem de votos em branco sobre o total de votos: {1}'.format(total*(nulo/100),total*(branco/100)))