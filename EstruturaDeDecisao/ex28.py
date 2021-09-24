#O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:
#                   Até 5 Kg              Acima de 5 Kg
#File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
#Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
#Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg
#Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção, 
# porém não há limites para a quantidade de carne por cliente. Se compra for feita no cartão Tabajara o cliente receberá ainda um 
# desconto de 5% sobre o total da compra. Escreva um programa que peça o tipo e a quantidade de carne comprada pelo usuário e gere um cupom fiscal, 
# contendo as informações da compra: tipo e quantidade de carne, preço total, tipo de pagamento, valor do desconto e valor a pagar.

tipo = input("Digite o tipo de carne que você deseja (File Duplo, Alcatra ou Picanha): ")
kg = int(input("Digite quantos kg você deseja comprar: "))
pag = input("Você deseja pagar no cartão?: ")

pag = pag.upper()
tipo = tipo.upper()

print("CUPOM FISCAL")

if tipo == "FILE DUPLO":
    print("Tipo de carne: File Duplo")
    if kg<=5:
        valor = kg*4.90
    else:
        valor = kg*5.80

elif tipo == "ALCATRA":
    print("Tipo de carne: Alcatra")
    if kg<=5:
        valor = kg*5.90
    else:
        valor = kg*6.80

elif tipo == "PICANHA":
    print("Tipo de carne: Picanha")
    if kg<5:
        valor = kg*6.90
    else:
        valor = kg*7.80

print('Você comprou um total de {0} kg, que deu um total de {1} reais'.format(kg, valor))

if pag == "S" or pag == "SIM":
    valor = valor-(valor*0.05)
    print('Como escolheu o metodo de pagamento por cartão você obteve 10% de desconto (desconto de {0:.2f} reais), que deu um total de: {1} reais'.format((valor*0.05),valor))
else:
    print('Como você escolheu não pagar pelo cartão o valor total da compra foi de: {0} reais'.format(valor))
