#Faça um programa que receba a temperatura média de cada mês do ano e armazene-as em uma lista. Após isto, calcule a média anual das temperaturas e 
# mostre todas as temperaturas acima da média anual, e em que mês elas ocorreram (mostrar o mês por extenso: 1 – Janeiro, 2 – Fevereiro, . . . ).

temp = []
mes = ['Janeiro','Fevereiro','Março','Abril','Maio','Junho','Julho','Agosto','Setembro','Outubro','Novembro','Dezembro']

for i in range(12):
    temp.append(float(input('Digite a temperatura média de {0}: '.format(mes[i]))))

media = sum(temp)/len(temp)

for i in range(len(temp)):
    z = temp[i]
    if z>media:
        print('Em {0} - {1} a temperatura ({2}) foi maior que a média anual {3:.2f}'.format(i+1, mes[i], z, media))
