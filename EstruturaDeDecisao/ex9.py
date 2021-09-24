#Faça um Programa que leia três números e mostre-os em ordem decrescente.

a = int(input("Digite o primeiro valor: "))
b = int(input("Digite o segundo valor: "))
c = int(input("Digite o terceiro valor: "))

if a < c:
    a, c = c, a

if a < b:
    a, b = b, a

if b < c:
    b, c = c, b

print('A ordem decrescente é: ', a, b, c)