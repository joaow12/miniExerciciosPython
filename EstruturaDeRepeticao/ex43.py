#Faça um programa que leia o código dos itens pedidos e as quantidades desejadas. Calcule e mostre o valor a ser pago por item (preço * quantidade) e o total geral do 
# pedido. Considere que o cliente deve informar quando o pedido deve ser encerrado.

lanche = ['Cachorro Quente', 'Bauru Simples', 'Bauru com ovo', 'Hambúguer', 'Cheeseburguer', 'Refrigerante']
preco = [1.20, 1.30, 1.50, 1.20, 1.30, 1.00]
cod = [100, 101, 102, 103, 104, 105]
pedido = []
cont = 0
resp = True

while resp != 'NAO' and resp != 'nao' and resp != 'n':
    print('Especificação | Código | Preço')
    print('Cachorro Quente | 100 | R$ 1,20 \nBauru Simples | 101 | R$ 1,30 \nBauru com ovo | 102 | R$ 1,50 \nHambúrguer | 103 | R$ 1,20 \nCheeseburguer | 104 | R$ 1,30 \nRefrigerante | 105 | R$ 1,00')

    codigo = int(input("Digite o código do pedido que você deseja: "))

    z = cod.index(codigo)

    qtde = int(input("Digite a quantos desse lanche você quer: "))

    valor = preco[z]*qtde

    pedido.append(valor)

    resp = input("Deseja fazer um novo pedido?: ")

while cont<len(pedido):
    print('Pedido n° {0} = R$ {1}'.format(cont+1, round(pedido[cont], 2)))
    cont += 1
print('Total: R$ {0}'.format(round(sum(pedido), 2)))