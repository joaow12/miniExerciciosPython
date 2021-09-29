#Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120

num = int(input("Digite o número que você deseja saber seu fatorial: "))

i = num-1

while i>0:
    num *= i
    i -= 1

print("O fatorial do número: ", num)