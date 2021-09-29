#Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor e a soma dos valores.

i = 1
soma = 0

count = int(input("Quantos números deseja digitar? "))

while i<=count:
    num = int(input("Digite um número: "))
    soma += num
    if i == 1:
        maior = num
        menor = num
    if num>maior:
        maior = num
    elif num<menor:
        menor = num
    i += 1

print('O maior valor: {0} \nO menor valor: {1} \nA soma de todos os números digitados: {2}'.format(maior, menor, soma))
