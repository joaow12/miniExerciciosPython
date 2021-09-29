#Numa eleição existem três candidatos. Faça um programa que peça o número total de eleitores. 
# Peça para cada eleitor votar e ao final mostrar o número de votos de cada candidato.

num = int(input("Digite quantos eleitores irão votar: "))
i = 1
votoUm = 0
votoDois = 0
votoTres = 0

while(i<=num):
    cand = int(input("Você vai votar no candidato 1, 2 ou 3?: "))
    if cand == 1:
        votoUm += 1
        i += 1
    elif cand == 2:
        votoDois += 1
        i += 1
    elif cand == 3:
        votoTres += 1
        i += 1
    else:
        print("Voto inválido (somente entre 1 e 3)")

print("TOTAL DE VOTOS: \nCandidato 1: {0} votos \nCandidato 2: {1} votos \nCandidato 3: {2} votos".format(votoUm, votoDois, votoTres))