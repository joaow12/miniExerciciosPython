#Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
#1 - o produto do dobro do primeiro com metade do segundo .
#2 - a soma do triplo do primeiro com o terceiro.
#3 - o terceiro elevado ao cubo.

num1 = int(input("Digite o primeiro valor inteiro: "))
num2 = int(input("Digite o segundo valor inteiro: "))
num3 = float(input("Digite um valor real: "))

print("O produto do dobro do primeiro com metade do segundo: ", ((num1*2)*(num2/2)))
print("A soma do triplo do primeiro com o terceiro: ", ((num1*3)+num3))
print("O terceiro elevado ao cubo: ", (num3**3))
