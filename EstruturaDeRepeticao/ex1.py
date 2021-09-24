#Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.

num = 20

while num>10 or num<0:
    num = int(input("Digite um número entre 0 e 10: "))
    if num>10 or num<0:
        print("Digite somente números entre 0 e 10")

print("Você encerrou o ciclo. \nNúmero digitado: ", num)
