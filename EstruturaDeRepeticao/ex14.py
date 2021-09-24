#Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares e a quantidade de números impares.

cont = 0
impar = 0
par = 0

while cont<10:
    cont += 1
    num = int(input("Digite um número: "))
    if num%2 == 0:
        par += 1
    else:
        impar += 1

print('A quantidade de números impares que você digiou foi: {0} \nA quantidade de números pares que você digitou foi: {1}'.format(impar, par))