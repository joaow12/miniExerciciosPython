#Os números primos possuem várias aplicações dentro da Computação, por exemplo na Criptografia. 
# Um número primo é aquele que é divisível apenas por um e por ele mesmo. Faça um programa que peça um número inteiro e determine se ele é ou não um número primo.

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