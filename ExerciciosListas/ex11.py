#Altere o programa anterior, intercalando 3 vetores de 10 elementos cada.

a = [1,3,5,7,9,11,13,15,17,19]
b = [2,4,6,8,10,12,14,16,18,20]
c = [21,22,23,24,25,26,27,28,29,30]
d = []

for i in range(10):
    d.append(a[i])
    d.append(b[i])
    d.append(c[i])


print('Vetor A: {0} \nVetor B: {1} \nVetor C: {2} \nVetor D: {3}'.format(a,b,c,d))