#Faça um Programa que leia três números e mostre o maior e o menor deles.

num1 = int(input("Digite o primeiro valor: "))
num2 = int(input("Digite o segundo valor: "))
num3 = int(input("Digite o terceiro valor: "))

maior = num1

if num2>num1:
    maior = num2

if num3>num1:
    maior = num3

print("O maior é: ", maior)

menor = num1

if num2<num1:
    menor = num2

if num3<num1:
    menor = num3

print("O menor é: ", menor)