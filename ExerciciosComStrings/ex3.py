#Nome na vertical. Faça um programa que solicite o nome do usuário e imprima-o na vertical.
nome = input("Digite seu nome: ")

nome = nome.upper()

for i in range(len(nome)):
    print(nome[i])