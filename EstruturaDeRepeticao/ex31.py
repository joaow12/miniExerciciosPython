#O Sr. Manoel Joaquim expandiu seus negócios para além dos negócios de 1,99 e agora possui uma loja de conveniências. 
# Faça um programa que implemente uma caixa registradora rudimentar. O programa deverá receber um número desconhecido de valores referentes aos preços das mercadorias. 
# Um valor zero deve ser informado pelo operador para indicar o final da compra. O programa deve então mostrar o total da compra e perguntar o valor em dinheiro que o 
# cliente forneceu, para então calcular e mostrar o valor do troco. Após esta operação, o programa deverá voltar ao ponto inicial, para registrar a próxima compra.

cont = 1

print("Lojas Tabajara")

valor = float(input("Produto 1 (caso queira encerrar a compra digite 0): R$"))
total = valor

while valor != 0:
    cont += 1
    valor = float(input('Produto {0} (caso queira encerrar a compra digite 0): R$'.format(cont)))
    total += valor

print('Valor total: R$ {0}'.format(total))
dinheiro = float(input("Digite quanto o cliente deu de dinheiro: R$"))
print('Troco: R${0}'.format(dinheiro-total))


