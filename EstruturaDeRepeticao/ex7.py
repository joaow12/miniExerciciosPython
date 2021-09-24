#Faça um programa que leia 5 números e informe o maior número.

num = []
i=1
maior = 0

while i<=5:
    i += 1
    z = int(input("Digite um número: "))
    if z>maior:
        maior = z

print("O maior número é: ", maior)