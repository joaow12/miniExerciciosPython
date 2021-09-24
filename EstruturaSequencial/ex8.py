#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.


salario = int(input("Digite quanto você ganhar por hora: "))
hora = int(input("Digite quantas horas você trabalha por mês: "))

print("Calculando o salario p/ hora mais as horas trabalhadas por mês da um total de : R$", (salario*hora))