#Faça um programa que carregue uma lista com os modelos de cinco carros (exemplo de modelos: FUSCA, GOL, VECTRA etc). 
# Carregue uma outra lista com o consumo desses carros, isto é, quantos quilômetros cada um desses carros faz com um litro de combustível. Calcule e mostre:
#O modelo do carro mais econômico;
#Quantos litros de combustível cada um dos carros cadastrados consome para percorrer uma distância de 1000 quilômetros e quanto isto custará, 
# considerando um que a gasolina custe R$ 2,25 o litro. Abaixo segue uma tela de exemplo. O disposição das informações deve ser o mais próxima possível ao exemplo. 
# Os dados são fictícios e podem mudar a cada execução do programa.

carros = ['Palio','Golf','Citroen','Civic','Ecosport']
gas = [10,13,8,9.5,11.5]

print('Relatório Final: ')
for i in range(len(gas)):
    z = 1000/gas[i]
    x = z*2.25
    if i == 0:
        menor = x
        y = carros[i]
    if menor>x:
        menor = x
        y = carros[i]
    print('{0} - {1} - {2} - {3:.1f} litros - R$ {4:.2f}'.format(i+1,carros[i],gas[i],z,x))

print('O menor consumo é do: {0}'.format(y))