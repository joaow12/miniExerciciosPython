#Faça um programa que leia dez conjuntos de dois valores, o primeiro representando o número do aluno e o segundo representando a sua altura em centímetros. 
# Encontre o aluno mais alto e o mais baixo. Mostre o número do aluno mais alto e o número do aluno mais baixo, junto com suas alturas.

cont = 1

while cont<=10:

    num = int(input("Digite o número do aluno: "))
    alt = int(input("Digite a altura do aluno: "))

    if cont == 1:
        maiorA = alt
        menorA = alt
    
    if alt>maiorA:
        maiorA = alt
        maiorC = num
    
    elif alt<menorA:
        menorA = alt
        menorC = num
    
    cont += 1

print('DADOS DOS ALUNOS: ')
print('O número do aluno mais alto é: {0} \nA altura do aluno mais alto é: {1} centimetros'.format(maiorC, maiorA))
print('O número do aluno mais baixo é: {0} \nA altura do aluno mais baixo é: {1} centimetros'.format(menorC, menorA))
