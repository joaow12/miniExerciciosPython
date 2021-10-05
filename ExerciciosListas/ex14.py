#Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
#"Telefonou para a vítima?"
#"Esteve no local do crime?"
#"Mora perto da vítima?"
#"Devia para a vítima?"
#"Já trabalhou com a vítima?" O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. 
# Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". 
# Caso contrário, ele será classificado como "Inocente".

print("Responda as proximas 5 perguntas com 'Sim' ou 'Não'")

countSim = 0

perguntas = ['Você telefonou para a vítima?: Sim ou Não?', 'Você esteve no local do crime?: Sim ou Não?', 'Você mora perto da vítima?: Sim ou Não?', 
'Você devia para a vítima?: Sim ou Não?', 'Você já trabalhou com a vítima?: Sim ou Não?']

for n in range(5):
    print(perguntas[n])
    resp = input("Sim ou Não?: ")
    resp = resp.upper()
    if resp == "SIM" or resp == "S":
        countSim = countSim+1

if countSim == 2:
    print("Por responder 2 questões como 'SIM' você foi classificado como 'Suspeita'")

elif countSim>=3 and countSim<=4:
    print("Por responder 3 ou 4 questões como 'SIM' você foi classificado como 'Cúmplice'")

elif countSim == 5:
    print("Por responder 5 questões como 'SIM' você foi classificado como 'Assassino'")

else:
    print("Por responder nenhuma ou somente uma questão como 'SIM' você foi classificado como 'Inocente'")