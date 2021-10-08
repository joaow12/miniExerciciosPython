#As Organizações Tabajara resolveram dar um abono aos seus colaboradores em reconhecimento ao bom resultado alcançado durante o ano que passou. 
# Para isto contratou você para desenvolver a aplicação que servirá como uma projeção de quanto será gasto com o pagamento deste abono.
#Após reuniões envolvendo a diretoria executiva, a diretoria financeira e os representantes do sindicato laboral, chegou-se a seguinte forma de cálculo:
#a.Cada funcionário receberá o equivalente a 20% do seu salário bruto de dezembro; a.O piso do abono será de 100 reais, isto é, 
# aqueles funcionários cujo salário for muito baixo, recebem este valor mínimo; Neste momento, não se deve ter nenhuma preocupação com colaboradores 
# com tempo menor de casa, descontos, impostos ou outras particularidades. Seu programa deverá permitir a digitação do salário de um número indefinido 
# (desconhecido) de salários. Um valor de salário igual a 0 (zero) encerra a digitação. Após a entrada de todos os dados o programa deverá calcular o valor 
# do abono concedido a cada colaborador, de acordo com a regra definida acima. Ao final, o programa deverá apresentar:
#O salário de cada funcionário, juntamente com o valor do abono;
#O número total de funcionário processados;
#O valor total a ser gasto com o pagamento do abono;
#O número de funcionário que receberá o valor mínimo de 100 reais;
#O maior valor pago como abono; A tela abaixo é um exemplo de execução do programa, apenas para fins ilustrativos


sal = []
abo = []
min = 0
cont = 0
z = True

while z!=0:
    z = float(input("Digite seu salário: "))
    if z == 0:
        break
    cont += 1
    if z<=500:
        sal.append(z)
        abo.append(100)
        min += 1
    else:
        sal.append(z)
        abo.append(z*0.2)

maior = max(abo)

print('Projeção de gastos com abono')
print('==================')
print('\nSalário   ---  Abono')
for i in range(len(sal)):
    print('R$ {0} - R$ {1}'.format(sal[i],abo[i]))
print('\nForam processados {0} colaboradores \nTotal gastos com abonos: R$ {1} \nValor minímo pago a {2} colaboradores \nMaior valor de abono pago: R$ {3}'.format(len(sal), sum(abo), min, maior))
