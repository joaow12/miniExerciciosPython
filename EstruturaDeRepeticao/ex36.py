#Desenvolva um programa que faça a tabuada de um número qualquer inteiro que será digitado pelo usuário, 
# mas a tabuada não deve necessariamente iniciar em 1 e terminar em 10, o valor inicial e final devem ser informados também pelo usuário

num = int(input("Digite o número que você deseja saber a tabuada: "))

ini = 5
fim = 1
i = 1

while ini>fim:

    ini = int(input("Digite onde você deseja iniciar a tabuada: "))
    fim = int(input("Digite onde você deseja terrminar a tabuada: "))

    if ini>fim:
        print("Número inicial maior que o final, digite novamente")

    else:
        print("A tabuada do número ", num)
        while ini<=fim:
            print('{0} x {1} = {2}'.format(num,ini,(num*ini)))
            ini += 1
        break
        