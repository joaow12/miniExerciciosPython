#Faça um programa que receba o valor de uma dívida e mostre uma tabela com os seguintes dados: valor da dívida, valor dos juros, quantidade de parcelas e valor da parcela

divida = float(input("Digite o valor da divida: "))

cont = 1
parc = 0
juros = 0.10

print("Valor da divida / Valor dos juros / Quantidade de parcelas / Valor da parcela")
print('R$ {0} / 0 / 1 / {1}'.format(divida, divida))

while cont<=4:
    if cont == 1:
        parc += 3
        valor = (divida+(divida*juros))/3
        print('R$ {0:.2f} / {1:.0f} / {2} / {3:.2f}'.format(divida+(divida*juros), divida*juros, parc, valor))
        cont += 1
    else:
        parc += 3
        juros += 0.05
        divida = divida+(divida*juros)
        valor = divida/parc
        print('R$ {0:.2f} / {1:.0f} / {2} / {3:.2f}'.format(divida, divida*juros, parc, valor))
        cont += 1