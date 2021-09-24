#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. 
# Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 
# 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
#salário bruto.
#quanto pagou ao INSS.
#quanto pagou ao sindicato.
#o salário líquido.
#calcule os descontos e o salário líquido

salarioH = int(input("Digite quanto você ganha por hora: "))
hora = int(input("Digite quantas horas você trabalha por mês: "))

salarioB = salarioH*hora
ir = salarioB*0.11
inss = salarioB*0.08
sindicato = salarioB*0.05

print("Salário Bruto: ", salarioB, "R$")
print("Quanto vai ser pago ao IR: ", ir, "R$")
print("Quanto vai ser pago ao INSS: ", inss, "R$")
print("Quanto vai ser pago ao Sindicato: ", sindicato, "R$")
print("Salário Liquido: ", (salarioB-ir-inss-sindicato), "R$")