#Altere o programa anterior para que ele aceite apenas números entre 0 e 1000.

i = 1
soma = 0

count = int(input("Quantos números deseja digitar? "))

while i<=count:
    num = int(input("Digite um número entre 0 e 1000: "))
    if num == 0 or num > 1000:
        print("Número inválido, digite novamente")
    else:
        soma += num
        if i == 1:
            maior = num
            menor = num
        if num>maior:
            maior = num
        elif num<menor:
            menor = num
        i += 1

print('O maior valor: {0} \nO menor valor: {1} \nA soma de todos os números digitados: {2}'.format(maior, menor, soma))