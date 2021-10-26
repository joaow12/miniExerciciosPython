#Palíndromo. Um palíndromo é uma seqüência de caracteres cuja leitura é idêntica se feita da direita para esquerda ou vice−versa. Por exemplo: 
# OSSO e OVO são palíndromos. Em textos mais complexos os espaços e pontuação são ignorados. A frase SUBI NO ONIBUS é o exemplo de uma frase palíndroma onde os 
# espaços foram ignorados. Faça um programa que leia uma seqüência de caracteres, mostre−a e diga se é um palíndromo ou não.
palavra = []
z = ""
y = ""

x = input("Digite a palavra: ")

for i in range(len(x)):
    if x[i] != " ":
        palavra.append(x[i])
        y += x[i]

palavra.reverse()

for i in range(len(palavra)):
    z += palavra[i]

if y == z:
    print('A palavra é um palíndromo')
else:
    print('A palavra não é um palíndromo')