#Faça um Programa que leia um vetor A com 10 números inteiros, calcule e mostre a soma dos quadrados dos elementos do vetor.

a = [5,4,10,8,9,6,13,5,3,2]

for i in range(len(a)):
    print('Soma do quadrado do {0}° número: {1}'.format(i+1, (a[i]**2)+(10*a[i])+25))
