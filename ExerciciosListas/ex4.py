#Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes.

x = []
cons = 0

for i in range(10):
    z = input("Digite um caractere: ")
    z = z.upper()
    x.append(z)

for i in range(len(x)):
    if x[i] != "A" and x[i] != "E" and x[i] != "I" and x[i] != "O" and x[i] != "U":
        print("Consoante: ", x[i])
        cons += 1

print('Teve ao todo {0} consoantes'.format(cons))