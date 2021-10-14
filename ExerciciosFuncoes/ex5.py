#Faça um programa com uma função chamada somaImposto. A função possui dois parâmetros formais: taxaImposto, que é a quantia de imposto sobre vendas expressa em porcentagem 
# e custo, que é o custo de um item antes do imposto. A função “altera” o valor de custo para incluir o imposto sobre vendas.

def somaImposto(custo,taxaImposto):
    custo += (taxaImposto/100)*custo
    return custo


custo = float(input("Digite o valor do item: "))
taxaImposto = int(input("Digite o taxa de imposto sobre o produto: %"))

print(somaImposto(custo, taxaImposto))