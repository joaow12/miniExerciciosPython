#Foram anotadas as idades e alturas de 30 alunos. Faça um Programa que determine quantos alunos com mais de 13 anos possuem altura inferior à média de altura desses alunos.

idade = []
altura = []
cont = 0

for i in range(30):
    z = int(input("Digite sua idade: "))
    idade.append(z)
    x = float(input("Digite sua altura: "))
    altura.append(x)

media = sum(altura)/len(altura)

for i in range(len(idade)):
    x = idade[i]
    z = altura[i]
    if x>13 and z<media:
        cont += 1

print('Tem {0} alunos com altura menor que a média da turma({1:.2f})'.format(cont, media))