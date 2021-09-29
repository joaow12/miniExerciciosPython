#O Departamento Estadual de Meteorologia lhe contratou para desenvolver um programa que leia as um conjunto indeterminado de temperaturas, e 
# informe ao final a menor e a maior temperaturas informadas, bem como a média das temperaturas.

i = 1
soma = 0

count = int(input("Quantas temperaturas deseja digitar? "))

while i<=count:
    num = float(input("Digite a temperatura: C°"))
    soma += num
    if i == 1:
        maior = num
        menor = num
    if num>maior:
        maior = num
    elif num<menor:
        menor = num
    i += 1

print('O maior temperatura: C°{0} \nA menor temperatura: C°{1} \nA média de todas as temperaturas que você digitou: C°{2:.2f}'.format(maior, menor, soma/count))
