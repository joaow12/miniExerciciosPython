#Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, 
# e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = nota1+nota2/2

if media>=9 and media<=10:
    print("Conceito A")
    print("APROVADO")

elif media>=7.5 and media<=9:
    print("Conceito B")
    print("APROVADO")

elif media>=6 and media<=7.5:
    print("Conceito C")
    print("APROVADO")

elif media>=4 and media<=6:
    print("Conceito D")
    print("REPROVADO")

elif media>=0 and media<=4:
    print("Conceito E")
    print("REPROVADO")

print("Média: ", media)