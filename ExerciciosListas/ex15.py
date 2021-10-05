#Faça um programa que leia um número indeterminado de valores, correspondentes a notas, encerrando a entrada de dados quando for informado um valor igual a -1 
# (que não deve ser armazenado). Após esta entrada de dados, faça:
#Mostre a quantidade de valores que foram lidos;
#Exiba todos os valores na ordem em que foram informados, um ao lado do outro;
#Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro;
#Calcule e mostre a soma dos valores;
#Calcule e mostre a média dos valores;
#Calcule e mostre a quantidade de valores acima da média calculada;
#Calcule e mostre a quantidade de valores abaixo de sete;
#Encerre o programa com uma mensagem;

resp = True
lista = []
cont = 0
contS = 0

while resp >=0:
    resp = int(input("Digite um número: "))
    if resp>=0:
        lista.append(resp)
        if resp<7:
            contS += 1

print('Foram lidos {0} valores \nValores na ordem digitados: {1}'.format(len(lista), lista))
print('Valores na ordem inversa: ')

for i in range(len(lista)):
    print(lista[len(lista)-1-i])

media = sum(lista)/len(lista)

print('Soma dos valores digitados: {0} \nMédia dos valores: {1:.2f}'.format(sum(lista), media))

for i in range(len(lista)):
    if lista[i]>media:
        cont += 1

print('Quantidade de valores acima da média calculada: {0} \nQuantidade de valores abaixo de sete: {1}'.format(cont, contS))
print('Programa encerrado!')