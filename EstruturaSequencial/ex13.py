#Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
#Para homens: (72.7*h) - 58
#Para mulheres: (62.1*h) - 44.7

gen = input("Digite o seu genero (H ou M): ")
altura = float(input("Digite sua altura: "))

if ((gen == "H") or (gen == "h")):
    print("Baseado na sua altura seu peso ideal é: ", (72.7*altura) - 58)

elif ((gen == "M") or (gen == "m")):
    print("Baseado na sua altura seu peso ideal é: ", (62.1*altura) - 44.7)