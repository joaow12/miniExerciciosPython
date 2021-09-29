#O Sr. Manoel Joaquim acaba de adquirir uma panificadora e pretende implantar a metodologia da tabelinha, que já é um sucesso na sua loja de 1,99. 
# Você foi contratado para desenvolver o programa que monta a tabela de preços de pães, de 1 até 50 pães, a partir do preço do pão informado pelo usuário

cont = 1
valor = float(input("Digite o preço do pão: "))

print('Lojas Quase Dois - Tabela de preços')

while cont<=50:
    print('{0} - R$ {1:.2f}'.format(cont, valor*cont))
    cont += 1