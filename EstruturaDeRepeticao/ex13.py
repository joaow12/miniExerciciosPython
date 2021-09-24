#Faça um programa que peça dois números, base e expoente, calcule e mostre o primeiro número elevado ao segundo número. Não utilize a função de potência da linguagem.

z = float(input("Digite o valor da base: "))
x = float(input("Digite o valor do expoente: "))

cont = 1
num = z

while cont<x:
    z = num*z
    cont += 1

print(z)