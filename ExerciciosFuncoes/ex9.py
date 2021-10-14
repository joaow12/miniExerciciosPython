#Reverso do número. Faça uma função que retorne o reverso de um número inteiro informado. Por exemplo: 127 -> 721.

def funcao(num):
    num = str(num)
    dividir = []
    b = ""
    for i in range(len(num)):
        dividir.append(num[i])

    dividir.reverse()

    for i in range(len(dividir)):
        b += dividir[i]
    return b

n = int(input("Digite um número: "))

print('{0} -> {1}'.format(n,funcao(n)))