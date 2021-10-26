#Jogo da palavra embaralhada. Desenvolva um jogo em que o usuário tenha que adivinhar uma palavra que será mostrada com as letras embaralhadas. 
# O programa terá uma lista de palavras lidas de um arquivo texto e escolherá uma aleatoriamente. O jogador terá seis tentativas para adivinhar a palavra. 
# Ao final a palavra deve ser mostrada na tela, informando se o usuário ganhou ou perdeu o jogo.
import random

palavras = ['RODA','CARRO','ALMOÇO','PEDRA','AMANHECER', 'ACADEMIA','JANTA','DOMINGO','ALMOFADA']
cont = 0
elemento = random.choice(palavras)
embaralhada = ''.join(random.sample(elemento,len(elemento)))

print('A PALAVRA ESCOLHIDA É: {0}'.format(embaralhada))
print('VOCÊ TEM 6 TENTATIVAS PARA DESCOBRIR A PALAVRA')

while cont<6:
    chute = input("Digite qual palavra você acha que é: ")
    chute = chute.upper()
    if chute != elemento:
        cont += 1
        print('Você errou pela {0}ª vez. Tente de novo!'.format(cont))
    else:
        print('PARABENS, VOCÊ ACERTOU A PALAVRA!')
        print('A PALAVRA ERA: {0}'.format(elemento))
        break
if cont == 6:
        print('VOCÊ NÃO CONSEGUIU ACERTAR A PALAVRA NAS 6 TENTATIVAS')
