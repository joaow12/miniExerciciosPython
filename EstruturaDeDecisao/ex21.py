#Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário a valor do saque e depois informar quantas notas de cada valor serão fornecidas. 
# As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. O valor mínimo é de 10 reais e o máximo de 600 reais. O programa não deve se preocupar com a quantidade de 
# notas existentes na máquina.
#Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50, uma nota de 5 e uma nota de 1;
#Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50, quatro notas de 10, uma nota de 5 e quatro notas de 1.

saque = int(input("Digite quanto você deseja sacar: "))

if saque<10 or saque>600:
    print("Valor inválido (Saque minimo 10 reais e maximo 600 reais)")
else:
    valor = saque
    cem = int(saque/100)
    saque = saque-(cem*100)
    cinquenta = int(saque/50)
    saque = saque-(cinquenta*50)
    dez = int(saque/10)
    saque = saque-(dez*10)
    cinco = int(saque/5)
    saque = saque-(cinco*5)
    um = saque
    print('Para sacar a quantida de {0} reais, o programa fornece {1} nota(s) de 100, {2} nota(s) de 50, {3} nota(s) de 10, {4} nota(s) de 5 e {5} nota(s) de 1' .format(valor, cem, cinquenta, dez, cinco, um))