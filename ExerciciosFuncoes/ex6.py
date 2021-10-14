#Faça um programa que converta da notação de 24 horas para a notação de 12 horas. Por exemplo, o programa deve converter 14:25 em 2:25 P.M. 
# A entrada é dada em dois inteiros. Deve haver pelo menos duas funções: uma para fazer a conversão e uma para a saída. Registre a informação A.M./P.M. 
# como um valor ‘A’ para A.M. e ‘P’ para P.M. Assim, a função para efetuar as conversões terá um parâmetro formal para registrar se é A.M. ou P.M. Inclua 
# um loop que permita que o usuário repita esse cálculo para novos valores de entrada todas as vezes que desejar.

resp = True

def conversaoH(horas,minutos):
    if horas>12 and horas<24:
        print('{0}:{1} PM'.format(horas-12,minutos))
    elif horas == 24:
        print('{0}:{1} AM'.format(horas-24,minutos))
    else:
        print('{0}:{1} AM'.format(horas,minutos))


while resp != "n":
    h = int(input("Digite as horas: "))
    x = int(input("Digite os minutos: "))

    conversaoH(h,x)

    resp = input("Deseja digitar novamente (s/n)? ")
