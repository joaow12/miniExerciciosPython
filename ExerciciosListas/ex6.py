#Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene num vetor a média de cada aluno, imprima o número de alunos com média maior ou igual a 7.0.

media = []
y = 0

for i in range(3):
    x = 0
    for i in range(4):
        z = float(input('Digite a {0}° nota: '.format(i+1)))
        x += z
    print('Média armazenada com sucesso!')
    x = x/4
    media.append(x)
    if x>= 7:
        y += 1

print('Na turma tivemos {0} alunos com média maior ou igual a 7'.format(y))

