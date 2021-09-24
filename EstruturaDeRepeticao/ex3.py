#Faça um programa que leia e valide as seguintes informações:
#Nome: maior que 3 caracteres;
#Idade: entre 0 e 150;
#Salário: maior que zero;
#Sexo: 'f' ou 'm';
#Estado Civil: 's', 'c', 'v', 'd';

nome = input("Digite um nome maior que 3 caracteres: ")
while len(nome)<=3:
    print("O nome tem menos que 3 caracteres")
    nome = input("Digite um nome maior que 3 caracteres: ")

idade = int(input("Digite uma idade entre 0 e 150 anos: "))
while (idade<0 or idade>150):
    print("A idade não está entre 0 e 150")
    idade = int(input("Digite uma idade entre 0 e 150 anos: "))

salario = float(input("Digite um salário maior que 0: "))
while salario<=0:
    print("Salário está abaixo de 1")
    salario = float(input("Digite um salário maior que 0: "))

sexo = input("Digite um sexo entre 'F' e 'M': ")
while sexo != "F" and sexo != "M":
    print("Sexo inválido")
    sexo = input("Digite um sexo entre 'F' e 'M': ")

estado = input("Digite um estado civil entre 'S', 'C', 'V' e 'D': ")
while estado != "S" and estado != "C" and estado != "V" and estado != "D":
    print("Estado Civil inválido")
    estado = input("Digite um estado civil entre 'S', 'C', 'V' e 'D': ")

print("Ciclo encerrado")
