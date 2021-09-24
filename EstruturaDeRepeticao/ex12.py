#Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10. 
# O usuário deve informar de qual numero ele deseja ver a tabuada. A saída deve ser conforme o exemplo abaixo

num = int(input("Digite o número que você deseja saber a tabuada: "))

i = 1

print("A tabuada do número ", num)
while i<=10:
    print('{0} x {1} = {2}'.format(num,i,(num*i)))
    i += 1