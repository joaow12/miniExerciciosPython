#Nome na vertical em escada invertida. Altere o programa anterior de modo que a escada seja invertida.

nome = str(input("Digite o seu nome: ")).upper()
cont = len(nome)
while cont>0:
    print(nome[:cont])
    cont -= 1