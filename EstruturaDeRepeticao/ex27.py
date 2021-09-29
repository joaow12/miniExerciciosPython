#Faça um programa que calcule o número médio de alunos por turma. Para isto, peça a quantidade de turmas e a quantidade de alunos para cada turma.
#  As turmas não podem ter mais de 40 alunos.

num = int(input("Digite quantas turmas tem: "))
total = 0
i = 1

while(i<=num):
    alunos = int(input('Digite quantos alunos tem na turma {0}: '.format(i)))
    if alunos>40:
        print("As turmas não podem ter mais que 40 alunos, digite novamente")
    else: 
        total += alunos
        i += 1

print('A média de alunos por turma é: {0:.2f}'.format(total/num))