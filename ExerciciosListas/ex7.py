#Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e os números.

num = []
multi = 1

for i in range(5):
    n = int(input("Digite um número: "))
    multi = multi * n
    num.append(n)

print('Soma dos números: {0} \nMultiplicação dos números: {1} \nO números digitados: {2}'.format(sum(num), multi, num))