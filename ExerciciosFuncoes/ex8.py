#Faça uma função que informe a quantidade de dígitos de um determinado número inteiro informado.

def funcao(num):
    num = str(num)
    return len(num)


num = int(input("Digite um número: "))

print('O número {0} tem {1} caracteres'.format(num,funcao(num)))
    