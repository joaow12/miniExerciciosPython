#Faça um programa que peça para n pessoas a sua idade, ao final o programa devera verificar se a média de idade da turma 
# varia entre 0 e 25,26 e 60 e maior que 60; e então, dizer se a turma é jovem, adulta ou idosa, conforme a média calculada.

cont = 0
soma = 0
resp = "S"

while resp == "SIM" or resp == "sim" or resp == "S" or resp == "s":
    idade = int(input("Digite a idade da pessoa: "))
    soma += idade
    cont += 1
    resp = input("Desejar digitar mais uma idade?: ")

media = soma/cont

if media>=0 and media<=25:
    print('A média de idade da sua turma é: {0} \nEla ficou na categoria "Jovem"'.format(media))
elif media>25 and media<=60:
    print('A média de idade da sua turma é: {0} \nEla ficou na categoria "Adulta"'.format(media))
else:
    print('A média de idade da sua turma é: {0} \nEla ficou na categoria "Idosa"'.format(media))