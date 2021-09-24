#A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,... Faça um programa capaz de gerar a série até o n−ésimo termo.

num1 = 0
num2 = 0

z = int(input("Digite o termo que deseja ser o final da sequencia de Fibonacci: "))

while(num2<=z):
    print(num2, end=', ')
    num2 = num2+num1
    num1 = num2-num1

    if num2 == 0:
        num2 = num2+1

