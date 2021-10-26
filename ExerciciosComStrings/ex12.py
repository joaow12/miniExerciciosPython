#Valida e corrige número de telefone. Faça um programa que leia um número de telefone, e corrija o número no caso deste conter somente 7 dígitos, 
# acrescentando o '3' na frente. O usuário pode informar o número com ou sem o traço separador.

telefone = input("Digite um número: ")
print('Telefone: ' + telefone[:3] + '-' + telefone[3:])
if len(telefone) == 7:
    print('Telefone possui 7 dígitos. Vou acrescentar o digito três na frente.')
    tel = '3'+telefone
    print('Telefone corrigido sem formatação: {0}'.format(tel))
    print('Telefone: ' + tel[:4] + '-' + tel[4:])
