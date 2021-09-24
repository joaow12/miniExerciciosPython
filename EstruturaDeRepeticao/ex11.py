#Altere o programa anterior para mostrar no final a soma dos números.

soma = 0

ini = int(input("Digite o valor inicial: "))
final = int(input("Digite o valor final: "))

while ini<=final:
    soma +=ini
    ini += 1

print("A soma do intervalo entre os números é: ", soma)