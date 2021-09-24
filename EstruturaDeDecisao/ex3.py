#Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.

sexo = input("Digite of sexo: ")

if sexo == "F" or sexo == "f" or sexo == "feminino" or sexo == "Feminino":
    print("Sexo feminino")
elif sexo == "M" or sexo == "m" or sexo == "masculino" or sexo == "Masculino":
    print("Sexo masculino")
else:
    print("Sexo inválido")