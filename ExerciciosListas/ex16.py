#Utilize uma lista para resolver o problema a seguir. Uma empresa paga seus vendedores com base em comissões. O vendedor recebe $200 por semana mais 9 por cento de suas 
# vendas brutas daquela semana. Por exemplo, um vendedor que teve vendas brutas de $3000 em uma semana recebe $200 mais 9 por cento de $3000, ou seja, um total de $470. 
# Escreva um programa (usando um array de contadores) que determine quantos vendedores receberam salários nos seguintes intervalos de valores:
#$200 - $299
#$300 - $399
#$400 - $499
#$500 - $599
#$600 - $699
#$700 - $799
#$800 - $899
#$900 - $999
#$1000 em diante

conts = [0,0,0,0,0,0,0,0,0]
sal = ["$200 - $299","$300 - $399","$400 - $499","$500 - $599","$600 - $699","$700 - $799","$800 - $899","$900 - $999","$1000 em diante"]
resp = "SIM"

while resp == "SIM" or resp == "S":
    z = 0
    z = float(input("Digite quanto você teve de vendar essa semana: "))
    z += 200+(z*0.09)
    if z>=200 and z<300:
        conts[0]+= 1
    elif z>=300 and z<400:
        conts[1]+= 1
    elif z>=400 and z<500:
        conts[2]+= 1
    elif z>=500 and z<600:
        conts[3]+= 1
    elif z>=600 and z<700:
        conts[4]+= 1
    elif z>=700 and z<800:
        conts[5]+= 1
    elif z>=800 and z<900:
        conts[6]+= 1
    elif z>=900 and z<1000:
        conts[7]+= 1
    elif z>=1000:
        conts[8]+= 1
    resp = input("Desejar digitar outro vendedor?:")
    resp = resp.upper()


for i in range(len(conts)):
    print('Quantidade de salários entre {0} = {1}'.format(sal[i], conts[i]))
