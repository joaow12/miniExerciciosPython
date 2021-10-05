#Faça um Programa que leia 20 números inteiros e armazene-os num vetor. Armazene os números pares no vetor PAR e os números IMPARES no vetor impar. Imprima os três vetores.

num = []
impar = []
par = []

for i in range(20):
    z = int(input("Digite um número: "))
    num.append(z)
    if z%2 != 0:
        impar.append(z)
    else:
        par.append(z)
    
print("Todos os números que você digitou: ", num)
print("Impares: ", impar)
print("Pares: ", par)
