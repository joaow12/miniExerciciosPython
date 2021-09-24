#Faça um Programa que peça dois números e imprima o maior deles.

num1 = int(input("Digite o primeiro valor: "))
num2 = int(input("Digite o segundo valor: "))

if num1>num2:
    print('O primeiro valor (%.0f) é o maior' %(num1))

elif num2>num1:
    print('O segundo valor (%.0f) é o maior' %(num2))

else:
    print('Ambos valores são iguais')