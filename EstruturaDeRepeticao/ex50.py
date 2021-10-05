#Sendo H= 1 + 1/2 + 1/3 + 1/4 + ... + 1/N, Faça um programa que calcule o valor de H com N termos.

n = 2
print("H = 1", end="")

while n<=10:
    print(' + {0}/{1}'.format(1, n), end=" ")
    n += 1