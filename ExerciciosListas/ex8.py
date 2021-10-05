#Faça um Programa que peça a idade e a altura de 5 pessoas, armazene cada informação no seu respectivo vetor. Imprima a idade e a altura na ordem inversa a ordem lida.

idade = []
altura = []

for i in range(5):
    idade.append(int(input("Digite sua idade: ")))
    altura.append(float(input("Digite sua altura: ")))

print("Idades na ordem inversa: ")
for valor in range(0, 5):
    print(idade[len(idade)-1-valor])

print("Alturas na ordem inversa: ")
for valor in range(0, 5):
    print(altura[len(altura)-1-valor])