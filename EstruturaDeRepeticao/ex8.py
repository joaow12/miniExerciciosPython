#Faça um programa que leia 5 números e informe a soma e a média dos números.

soma = 0
i = 1

while i<=5:
    i += 1
    z = int(input("Digite um número: "))
    soma += z

media = soma/5

print('A soma dos números é: {0} \nA média dos números é: {1}'.format(soma, media))