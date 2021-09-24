#Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.

pProd = float(input("Digite o valor do primeiro produto: "))
sProd = float(input("Digite o valor do segundo produto: "))
tProd = float(input("Digite o valor do terceiro produto: "))

barato = pProd

if sProd<barato:
    barato = sProd

if tProd<barato:
    barato = tProd

print("O mais barato é o :", barato)