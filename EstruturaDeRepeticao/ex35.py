#Encontrar números primos é uma tarefa difícil. Faça um programa que gera uma lista dos números primos existentes entre 1 e um número inteiro informado pelo usuário.

cont = 1
div = 0
z = 1
primos = []

num = int(input("Digite um número: "))

while z<=num:
    if z%2 == 1 and z!= 2:
        primos.append(z)
    z += 1

print(primos)