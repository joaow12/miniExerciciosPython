#Faça um Programa que leia três números e mostre o maior deles.

num1 = int(input("Digite o primeiro valor: "))
num2 = int(input("Digite o segundo valor: "))
num3 = int(input("Digite o terceiro valor: "))

if num1>num2 and num1>num3:
    print('O primeiro valor (%.0f) é o maior' %(num1))

elif num2>num1 and num2>num3:
    print('O segundo valor (%.0f) é o maior' %(num2))

elif num3>num1 and num3>num2:
    print('O terceiro valor (%.0f) é o maior' %(num3))

else:
    print('Todos valores são iguais')