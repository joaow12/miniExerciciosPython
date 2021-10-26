#Conta espaços e vogais. Dado uma string com uma frase informada pelo usuário (incluindo espaços em branco), conte:
#quantos espaços em branco existem na frase.
#quantas vezes aparecem as vogais a, e, i, o, u.


x = input("Digite uma frase aleatória: ")
x = x.upper()
esp = 0
vog = 0

for i in range(len(x)):
    if x[i] == " ":
        esp += 1
    elif x[i] == "A" or x[i] == "E" or x[i] == "I" or x[i] == "O" or x[i] == "U":
        vog += 1

print('A frase tem {0} espaços e {1} vogais'.format(esp, vog))