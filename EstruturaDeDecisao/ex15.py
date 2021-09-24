#Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo. Indique, 
# caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
#Dicas:
#Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
#Triângulo Equilátero: três lados iguais;
#Triângulo Isósceles: quaisquer dois lados iguais;
#Triângulo Escaleno: três lados diferentes;

ladoA = float(input("Digite o primeiro lado do triangulo: "))
ladoB = float(input("Digite o segundo lado do triangulo: "))
ladoC = float(input("Digite o terceiro lado do triangulo: "))

if (ladoA + ladoB < ladoC) or (ladoA + ladoC < ladoB) or (ladoB + ladoC < ladoA):
    print('Nao é um triangulo')

elif (ladoA == ladoB) and (ladoA == ladoC) :
    print('Equilatero')

elif (ladoA==ladoB) or (ladoA==ladoC) or (ladoB==ladoC):
    print('Isósceles')
    
else:
    print('Escaleno')