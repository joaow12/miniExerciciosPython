#Verificação de CPF. Desenvolva um programa que solicite a digitação de um número de CPF no formato xxx.xxx.xxx-xx e indique se é um número válido ou 
# inválido através da validação dos dígitos verificadores edos caracteres de formatação.

x = input("Digite o CPF no formato 'xxx.xxx.xxx-xx': ")

if len(x) == 14 and x[3] == "." and x[7] == "." and x[11] == "-":
    print('CPF válido')
else:
    print('CPF inválido')