#Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c. O programa deverá pedir os valores de a, b e c e fazer as consistências, 
# informando ao usuário nas seguintes situações:
#Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa não deve fazer pedir os demais valores, sendo encerrado;
#Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre o programa;
#Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
#Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;
import math

a = float(input("Digite o primeiro valor: "))

if a == 0:
    print("Como o valor foi 0 a equação não é de 2° grau")
else:
    b = float(input("Digite o segundo valor: "))
    c = float(input("Digite o terceiro valor: "))

    eq = b*b - (4*a*c)

    if eq<0:
        print("Delta negativo. A equação não possui raizes reais")
    
    elif eq == 0:
        print("Delta zerado. A equação possui apenas uma raiz real")
        raiz = ((-1)*b + math.sqrt(eq))/(2*a)
        print(raiz)

    else:
        raiz1 = ((-1)*b + math.sqrt(eq))/(2*a)
        raiz2 = ((-1)*b - math.sqrt(eq))/(2*a)
        print("A equação possui duas raizes que são:", raiz1, "e", raiz2)