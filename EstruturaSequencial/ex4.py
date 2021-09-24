#Faça um Programa que peça as 4 notas bimestrais e mostre a média.

soma = 0
num = 0

for i in range(4):
    num = int(input("Digite uma nota: "))
    soma = soma+num

print("A média das notas é: ", (soma/4))

