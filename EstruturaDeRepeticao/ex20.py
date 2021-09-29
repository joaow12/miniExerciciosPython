#Altere o programa de cálculo do fatorial, permitindo ao usuário calcular o fatorial várias vezes e limitando o fatorial a números inteiros positivos e menores que 16.

resp = "S"

while resp == "S" or resp == "SIM" or resp == "s" or resp == "sim" :

    num = int(input("Digite o número que você deseja saber seu fatorial (entre 1 e 15): "))

    if num>0 and num<16:

        i = num-1

        while i>0:
            num *= i
            i -= 1

        print("O fatorial do número: ", num)
    
    else:
        print("Número inválido (somente entre 1 e 15)")
    
    resp = input("Deseja calcular outra vez? ")

print("Programa encerrado")