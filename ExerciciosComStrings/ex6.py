#Data por extenso. Faça um programa que solicite a data de nascimento (dd/mm/aaaa) do usuário e imprima a data com o nome do mês por extenso.

mes = ['Janeiro','Fevereiro','Março','Abril','Maio','Junho','Julho','Agosto','Setembro','Outubro','Novembro','Dezembro']

x = input("Digite um data 'dd/mm/aaaa': ")

print(x.split('/')[0], 'de',mes[(int(x.split("/")[1])-1)],"de",x.split("/")[2])