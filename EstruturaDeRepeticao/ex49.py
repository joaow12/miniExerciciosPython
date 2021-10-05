#Faça um programa que mostre os n termos da Série a seguir:
#S = 1/1 + 2/3 + 3/5 + 4/7 + 5/9 + ... + n/m.

anterior = 1
proximo = 1
n = int(input("Digite até onde você deseja ver a sequencia: "))
s = 0

print("S = ", end="")
while anterior<=n:
    s += anterior/proximo
    print('{0}/{1}'.format(anterior, proximo),end=" + ")
    anterior += 1
    proximo +=2

print('\nSoma = {0:.2f}'.format(s))