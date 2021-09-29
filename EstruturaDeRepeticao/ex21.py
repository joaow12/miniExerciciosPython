#Faça um programa que peça um número inteiro e determine se ele é ou não um número primo. Um número primo é aquele que é divisível somente por ele mesmo e por 1.


num = int(input("Digite um número: "))

cont = 1
div = 0

if num>0:

    while cont<=num:
        if num%cont == 0:
            div += 1
        cont += 1
    
    if div == 2:
        print("É primo")
    
    else:
        print("Não é primo")
        