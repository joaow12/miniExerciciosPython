#Faça um programa, com uma função que necessite de três argumentos, e que forneça a soma desses três argumentos.

def soma(z,y,x):
    soma = z+y+x
    print(soma)

z = int(input("Digite um número: "))
y = int(input("Digite um número: "))
x = int(input("Digite um número: "))
soma(z,y,x)