#Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, 
# que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto, mas não é descontado 
# (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os descontos. O programa deverá pedir ao usuário o valor da sua hora e a 
# quantidade de horas trabalhadas no mês.
#Desconto do IR:
#Salário Bruto até 900 (inclusive) - isento
#Salário Bruto até 1500 (inclusive) - desconto de 5%
#Salário Bruto até 2500 (inclusive) - desconto de 10%
#Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, dispostas conforme o exemplo abaixo. 
# No exemplo o valor da hora é 5 e a quantidade de hora é 220.

salario = int(input("Digite quanto você ganhar por hora: "))
hora = int(input("Digite quantas horas você trabalha por mês: "))

sBruto = salario*hora

if sBruto>900 and sBruto<=1500:
    ir = sBruto*0.05

elif sBruto>1500 and sBruto<=2500:
    ir = sBruto*0.10

elif sBruto>2500:
    ir = sBruto*0.20

inss = sBruto*0.10
fgts = sBruto*0.11
sLiquido = (sBruto-ir)-inss

print("O salário bruto é: ", sBruto, "R$")
print("(-) Imposto de renda: ", ir, "R$")
print("(-) INSS: ", inss, "R$")
print("FGTS: ", fgts, "R$")
print("Total descontado: ", ir+inss, "R$")
print("Salário Liquido: ", sLiquido, "R$")