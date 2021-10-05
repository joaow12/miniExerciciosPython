#Faça um Programa que leia dois vetores com 10 elementos cada. Gere um terceiro vetor de 20 elementos, 
# cujos valores deverão ser compostos pelos elementos intercalados dos dois outros vetores.

a = [1,3,5,7,9,11,13,15,17,19]
b = [2,4,6,8,10,12,14,16,18,20]
c = []

for i in range(10):
    c.append(a[i])
    c.append(b[i])

print('Vetor A: {0} \nVetor B: {1} \nVetor C: {2}'.format(a,b,c))
