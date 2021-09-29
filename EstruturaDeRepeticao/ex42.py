#Faça um programa que leia uma quantidade indeterminada de números positivos e conte quantos deles estão nos seguintes intervalos: [0-25], [26-50], [51-75] e [76-100]. 
# A entrada de dados deverá terminar quando for lido um número negativo.

num = True
n25 = []
n50 = []
n75 = []
n100 = []

while num>0:
    num = int(input("Digite um número (caso queira encerrar o programa digite 0): "))
    if num>=0 and num<=25:
        n25.append(num)
    elif num>25 and num<=50:
        n50.append(num)
    elif num>50 and num<=75:
        n75.append(num)
    elif num>75 and num<=100:
        n100.append(num)
    
print('Números entre [0-25]: {0} '.format(len(n25)))
print('Números entre [26-50]: {0} '.format(len(n50)))
print('Números entre [51-75]: {0} '.format(len(n75)))
print('Números entre [76-100]: {0} '.format(len(n100)))
