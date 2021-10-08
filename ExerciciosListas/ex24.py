#Faça um programa que simule um lançamento de dados. Lance o dado 100 vezes e armazene os resultados em um vetor . Depois, mostre quantas vezes cada valor foi conseguido. 
# Dica: use um vetor de contadores(1-6) e uma função para gerar numeros aleatórios, simulando os lançamentos dos dados.

import random

nums = [0,0,0,0,0,0]
z = 0

while z<100:
    x = random.randint(0,5)
    nums[x] += 1
    z += 1

for i in range(len(nums)):
    print('Número {0} foi conseguido {1} vezes'.format(i+1, nums[i]))
