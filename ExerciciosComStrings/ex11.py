#Jogo de Forca. Desenvolva um jogo da forca. O programa terá uma lista de palavras lidas de um arquivo texto e escolherá uma aleatoriamente. O jogador poderá errar 6 vezes antes de ser enforcado.
import random

palavras = ['RODA','CARRO','ALMOÇO','PEDRA','AMANHECER', 'ACADEMIA','JANTA','DOMINGO','ALMOFADA']
cont = 0
escolhido = []
acerto = 0
elemento = random.choice(palavras)

for i in range(len(elemento)):
    escolhido.append('_')

print('JOGO DA FORCA, VOCÊ TEM 6 TENTATIVAS DE DESCOBRIR A PALAVRA')
print('A PALAVRA ESCOLHIDA TEM {0} LETRAS'.format(len(elemento)))

while cont<6:
    letra = input("Digite uma letra: ")
    letra = letra.upper()
    if letra in elemento:
        index = elemento.index(letra)
        acerto += 1
        escolhido[index] = letra
        print(escolhido)
    else:
        cont += 1
        print('Você errou pela {0}ª vez. Tente de novo!'.format(cont))
    if acerto == len(elemento):
        print('PARABENS, VOCÊ ACERTOU TODAS AS LETRAS')
        print('A PALAVRA ERA: {0}'.format(elemento))
        break
if cont == 6:
        print('VOCÊ NÃO CONSEGUIU ACERTAR A PALAVRA NAS 6 TENTATIVAS')