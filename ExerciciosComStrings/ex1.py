#Tamanho de strings. Faça um programa que leia 2 strings e informe o conteúdo delas seguido do seu comprimento. 
# Informe também se as duas strings possuem o mesmo comprimento e são iguais ou diferentes no conteúdo.
#Compara duas strings
#String 1: Brasil Hexa 2006
#String 2: Brasil! Hexa 2006!
#Tamanho de "Brasil Hexa 2006": 16 caracteres
#Tamanho de "Brasil! Hexa 2006!": 18 caracteres
#As duas strings são de tamanhos diferentes.
#As duas strings possuem conteúdo diferente.

texto1 = "Brasil Hexa 2006"
texto2 = "Brasil! Hexa 2006!"

print('tamanho de "{0}": {1}'.format(texto1, len(texto1)))
print('tamanho de "{0}": {1}'.format(texto2, len(texto2)))

if len(texto1) != len(texto2):
    print('As duas strings são de tamanhos diferentes.')

if texto1 != texto2:
    print('As duas strings possuem conteúdo diferente.')