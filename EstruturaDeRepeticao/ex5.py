#Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais. Valide a entrada e permita repetir a operação.

resp = "S"
anos = 0

while resp =="S" or resp =="SIM":

    a = int(input("Digite a população do país A: "))
    taxaA = int(input("Digite a taxa de crescimento em % do país A: "))

    while a==0 and taxaA==0:
        print("Valor inválido")
        a = int(input("Digite a população do país A: "))
        taxaA = int(input("Digite a taxa de crescimento em % do país A: "))

    b = int(input("Digite a população do país B: "))
    taxaB = int(input("Digite a taxa de crescimento em % do país B: "))

    while b==0 and taxaB==0:
        print("Valor inválido")
        b = int(input("Digite a população do país A: "))
        taxaB = int(input("Digite a taxa de crescimento em % do país B: "))

    if b>a:
        while b>a:
            a = a+(a*(taxaA/100))
            b = b+(b*(taxaB/100))
            anos += 1
    elif b<a:
        while b<a:
            a = a+(a*(taxaA/100))
            b = b+(b*(taxaB/100))
            anos += 1
    
    print('Foram necessarios {0} anos para o país com menor população ultrapassar o com maior pais em população \nPopulação do país A: {1:.0f} \nPopulação do país B: {2:.0f}'.format(anos, a, b))
    resp = input("Deseja fazer novamente?: ")
    resp = resp.upper()

print("Programa encerrado")