#Faça um Programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.

num = int(input("Digite um valor: "))

if num == 1:
    print("Domingo")
elif num == 2:
    print("Segunda-Feira")
elif num == 3:
    print("Terça-Feira")
elif num == 4:
    print("Quarta-Feira")
elif num == 5:
    print("Quinta-Feira")
elif num == 6:
    print("Sexta-Feira")
elif num == 7:
    print("Sábado")
else:
    print("Valor inválido")