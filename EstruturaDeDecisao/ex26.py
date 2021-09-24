#Um posto está vendendo combustíveis com a seguinte tabela de descontos:
#Álcool:
#até 20 litros, desconto de 3% por litro
#acima de 20 litros, desconto de 5% por litro
#Gasolina:
#até 20 litros, desconto de 4% por litro
#acima de 20 litros, desconto de 6% por litro 
#Escreva um algoritmo que leia o número de litros vendidos, o tipo de combustível 
#(codificado da seguinte forma: A-álcool, G-gasolina), calcule e imprima o valor a ser pago pelo cliente sabendo-se que o preço do 
#litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90.

comb = input("Digite qual combustivel você deseja comprar: Álcool ou Gasolina? ")
litro = int(input("Digite quantos litros você deseja comprar: "))

comb = comb.upper()

if comb == "ÁLCOOL" or comb == "ALCOOL" or comb == "A":
    qtde = litro*1.9
    if litro<=20:
        qtde -= 1.9 * litro * 0.03
    elif litro>20:
        qtde -= 1.9 * litro * 0.05

elif comb == "GASOLINA" or comb == "G":
    qtde = litro*2.50
    if litro<=20:
        qtde -= 2.5 * litro * 0.04
    elif litro>20:
        qtde -= 2.5 * litro * 0.06


print('O total a pagar é {:.2f} reais'.format(qtde))