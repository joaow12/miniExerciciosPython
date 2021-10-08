#Sua organização acaba de contratar um estagiário para trabalhar no Suporte de Informática, com a intenção de fazer um levantamento nas sucatas encontradas nesta área. 
# A primeira tarefa dele é testar todos os cerca de 200 mouses que se encontram lá, testando e anotando o estado de cada um deles, para verificar o que se pode aproveitar 
# deles.
#Foi requisitado que você desenvolva um programa para registrar este levantamento. O programa deverá receber um número indeterminado de entradas, 
# cada uma contendo: um número de identificação do mouse o tipo de defeito: necessita da esfera;
#necessita de limpeza; a.necessita troca do cabo ou conector; a.quebrado ou inutilizado Uma identificação igual a zero encerra o programa. 

defeito = ['Necessita de esfera','Necessita de limpeza','Necessita de troca de cabo ou conector','Quebrado ou unitilizado']
cont = [0,0,0,0]
z = 0
x = 0

while z<=200 or x!=0:
    print('Código de defeito: ')
    for i in range(len(defeito)):
        print('{0} - {1}'.format(i+1, defeito[i]))
    x = int(input("Digite o código de defeito desse mouse: "))
    if x == 0:
        print('Programa encerrado')
        break
    elif x>0 and x<=4:
        cont[x-1] += 1
        z += 1
    else:
        print('Código inválido')

print('Quantidade de mouses: {0}'.format(z))
print('Situação / Quantidade / Percentual')
for i in range(len(defeito)):
    porc = (cont[i]*100)/sum(cont)
    print('{0} - {1} / {2} / {3:.0f}%'.format(i+1, defeito[i], cont[i], porc))
