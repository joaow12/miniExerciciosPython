#Faça um Programa que leia 4 notas, mostre as notas e a média na tela.

notas = []

for i in range(4):
    z = int(input("Digite a nota: "))
    notas.append(z)

for i in range(4):
    print('{0}° nota: {1}'.format(i, notas[i]))

media = sum(notas)

print("Média das notas: ", media/4)