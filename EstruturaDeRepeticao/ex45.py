#Desenvolver um programa para verificar a nota do aluno em uma prova com 10 questões, o programa deve perguntar ao aluno a resposta de cada questão e ao final 
# comparar com o gabarito da prova e assim calcular o total de acertos e a nota (atribuir 1 ponto por resposta certa). Após cada aluno utilizar o sistema deve ser 
# feita uma pergunta se outro aluno vai utilizar o sistema. Após todos os alunos terem respondido informar:
#Maior e Menor Acerto;
#Total de Alunos que utilizaram o sistema;
#A Média das Notas da Turma.
#Após concluir isto você poderia incrementar o programa permitindo que o professor digite o gabarito da prova antes dos alunos usarem o programa.

gab = []
alunos = []
certo = 0
media = 0
resp = True

for i in range(10):
    print("Questão: ", i + 1)
    x = (input("Digite a alternativa correta: "))
    x = x.upper()
    gab.append(x)

while resp != "n":
    for i in range(len(gab)):
        z = input('Qual foi sua resposta para a pergunta {0}: '.format(i+1))
        z = z.upper()
        if z == gab[i]:
            certo += 1
    alunos.append(certo)
    resp = input("Outro aluno deseja utilizar o sistema?: ")
    certo = 0


for i in range(len(alunos)):
    if i == 0:
        maior = alunos[i]
        menor = alunos[i]
    if maior<alunos[i]:
        maior = alunos[i]
    elif menor>alunos[i]:
        menor = alunos[i]

total = len(alunos)
media = sum(alunos)/total

print('O aluno que teve mais acertos foi {0} questões \nO que teve menos acertos foi {1} questões'.format(maior, menor))
print('O total de alunos que utilizaram o sistema foi {0} \nA média da turma foi {1:.2f}'.format(total, media))
