#Faça um programa que peça um numero inteiro positivo e em seguida mostre este numero invertido.

a = int(input("Digite um número inteiro positivo: "))

if a <0:
    print("Somente número positivo")
else:
    z = str(a)
    b = ""
    dividir = []

    for i in range(len(z)):
        dividir.append(z[i])

    dividir.reverse()

    for i in range(len(dividir)):
        b += dividir[i]

    print(b)