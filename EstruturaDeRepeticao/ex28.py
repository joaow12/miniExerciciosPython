#Faça um programa que calcule o valor total investido por um colecionador em sua coleção de CDs e o valor médio gasto em cada um deles. 
# O usuário deverá informar a quantidade de CDs e o valor para em cada um.

cd = float(input("Digite a quantidade de CDs: "))

x = 1
total = 0

while(x<=cd):
    valor = float(input("Digite o valor do CD: "))
    total += valor
    x +=1

print('O valor total investido: {0} reais \nO valor médio gasto em cada um deles: {1}'.format(total, total/cd))

