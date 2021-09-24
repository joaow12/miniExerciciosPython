#Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar. O resultado da operação deve ser acompanhado de uma frase 
# que diga se o número é:
#par ou ímpar;
#positivo ou negativo;
#inteiro ou decimal.

x = float(input("Digite o primeiro número: "))
y = float(input("Digite o segundo número: "))
op = input("Digite qual operação você quer fazer (+, -, / ou *): ")

z = 0

if op == "+":
    z = x+y
    print("Resultado da soma dos números: ", z)

elif op == "-":
    z = x-y
    print("Resultado da subtração dos números: ", z)

elif op == "/":
    z = x/y
    print("Resultado da divisão dos números: ", z)

elif op == "*":
    z = x*y
    print("Resultado da multiplicação dos números: ", z)

else:
    print("Operador inválido")

if z%2 != 0:
    print("Número par")
else:
    print("Número impar")

if z>0:
    print("Número positivo")
else:
    print("Número negativo")

if z == round(z):
    print("Número inteiro")
else:
    print("Número decimal")