#Altere o programa de cálculo dos números primos, informando, caso o número não seja primo, por quais número ele é divisível.

num = int(input("Digite um número: "))

cont = 0
div = 0

if num>0:

    while cont<=num or cont<2:
        cont += 1
        if num%cont == 0:
            print("Múltiplo de",cont)
            div += 1
    
    if div == 2:
        print("É primo")
    
    else:
        print("Não é primo")
        print('Tem {0} múltiplos acima de 2 e abaixo de: {1}'.format(div, num))