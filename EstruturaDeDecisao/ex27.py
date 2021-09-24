#Uma fruteira está vendendo frutas com a seguinte tabela de preços:
#                   Até 5 Kg              Acima de 5 Kg
#Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
#Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg
#Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00, 
# receberá ainda um desconto de 10% sobre este total. Escreva um algoritmo para ler a quantidade (em Kg) de morangos e 
# a quantidade (em Kg) de maças adquiridas e escreva o valor a ser pago pelo cliente.

morango = int(input("Digite quantos kg de morango você deseja comprar: "))
maca = int(input("Digite quantos kg de morangos você deseja comprar: "))

kgTotal = morango+maca

if morango<=5:
    valorMorango = morango*2.50
else:
    valorMorango = morango*2.20

if maca<=5:
    valorMaca = maca*1.80
else:
    valorMaca = maca*1.50

valorTotal = valorMorango+valorMaca

print('Você comprou {0} kg de morangos, que deu um total de {1} reais'.format(morango, valorMorango))
print('Você comprou {0} kg de maçãs, que deu um total de {1} reais'.format(maca, valorMaca))
print('Juntando as duas compras deu um total de {0} kg que da um total de {1} reais'.format(kgTotal, valorTotal))

if kgTotal>8 or valorTotal>25:
    valorTotal = valorTotal-(valorTotal*0.10)
    print('Por ter passado de 8kg no total (ou 25 reais) você conseguiu um desconto de 10% sobre o valor total, que da um valor final de: {0} reais'.format(valorTotal) )