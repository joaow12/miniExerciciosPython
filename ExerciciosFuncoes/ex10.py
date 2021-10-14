#Jogo de Craps. Faça um programa de implemente um jogo de Craps. O jogador lança um par de dados, obtendo um valor entre 2 e 12. Se, na primeira jogada, 
# você tirar 7 ou 11, você um "natural" e ganhou. Se você tirar 2, 3 ou 12 na primeira jogada, isto é chamado de "craps" e você perdeu. 
# Se, na primeira jogada, você fez um 4, 5, 6, 8, 9 ou 10,este é seu "Ponto". Seu objetivo agora é continuar jogando os dados até tirar este número novamente. 
# Você perde, no entanto, se tirar um 7 antes de tirar este Ponto novamente.
import random


def craps(dadoUm,dadoDois,ini):
    if ini == "s":
        dadoUm = random.randint(1,6)
        dadoDois = random.randint(1,6)
        prox = 0
        cont = 2
        soma = dadoUm+dadoDois
        print('1° JOGADA')
        if soma == 11 or soma == 7:
            print('Você tirou {0}, "Natural", VOCÊ GANHOU!'.format(soma))
        elif soma == 2 or soma == 3 or soma == 12:
            print('Você tirou {0}, "Craps", VOCÊ PERDEU!'.format(soma))
        else:
            print('Você tirou {0}, irá jogar novamente até tirar o mesmo número, mas se tirar 7 você perde'.format(soma))
            while prox != soma:
                print('{0}° JOGADA'.format(cont))
                cont += 1
                dadoUm = random.randint(1,6)
                dadoDois = random.randint(1,6)
                prox = dadoUm+dadoDois
                if prox == 7:
                    print('Você tirou {0}, VOCÊ PERDEU!'.format(prox))
                    break
                elif prox == soma:
                    print('Você conseguiu repetir o mesmo número ({0}), VOCÊ GANHOU!'.format(prox))
                    break
                else:
                    print('Você tirou {0}!'.format(prox))

z = 0
x = 0

y = input("Deseja iniciar (s/n): ")

craps(x,z,y)
