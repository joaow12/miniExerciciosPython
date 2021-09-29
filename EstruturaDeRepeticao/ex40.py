#Foi feita uma estatística em cinco cidades brasileiras para coletar dados sobre acidentes de trânsito. Foram obtidos os seguintes dados:
#Código da cidade;
#Número de veículos de passeio (em 1999);
#Número de acidentes de trânsito com vítimas (em 1999). Deseja-se saber:
#Qual o maior e menor índice de acidentes de transito e a que cidade pertence;
#Qual a média de veículos nas cinco cidades juntas;
#Qual a média de acidentes de trânsito nas cidades com menos de 2.000 veículos de passeio.

cont = 1
media = 0
mediaCont = 0

while cont<=5:

    cod = int(input("Digite o número da cidade: "))
    vei = int(input("Digite a quantidade de veiculos de passeio que a cidade tem: "))
    aci = int(input("Digite a quantidade de acidentes de transitos com vitimas na cidade: "))

    if cont == 1:
        maiorAci = aci
        menorAci = aci
    
    if vei<2000:
        mediaAci = aci
        mediaCont += 1
    
    if aci>maiorAci:
        maiorAci = aci
        maiorNum = cod
    
    elif aci<menorAci:
        menorAci = aci
        menorNum = cod
    
    media += vei
    
    cont += 1

print('DADOS DAS CIDADES: ')
print('A cidade com maior número de acidentes é: n°{0} com {1} acidentes'.format(maiorNum, maiorAci))
print('A cidade com menor número de acidentes é: n°{0} com {1} acidentes'.format(menorNum, menorAci))
print('A média de veiculos das 5 cidades juntas é: {0:.2f}'.format(media/5))
print('A média de acidentes de trânsito nas cidades com menos de 2.000 veículos de passeio é: {0:.2f}'.format(mediaAci/mediaCont))
