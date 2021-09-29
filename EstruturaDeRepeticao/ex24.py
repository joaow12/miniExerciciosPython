#Faça um programa que calcule o mostre a média aritmética de N notas.

cont = 0
soma = 0
resp = "S"

while resp == "SIM" or resp == "sim" or resp == "S" or resp == "s":
    nota = int(input("Digite a nota: "))
    soma += nota
    cont += 1
    resp = input("Desejar digitar mais uma nota?: ")

print('A média das {0} notas que você digitou é: {1}'.format(cont, (soma/cont)))