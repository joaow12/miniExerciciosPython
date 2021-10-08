#A ACME Inc., uma empresa de 500 funcionários, está tendo problemas de espaço em disco no seu servidor de arquivos. Para tentar resolver este problema, 
# o Administrador de Rede precisa saber qual o espaço ocupado pelos usuários, e identificar os usuários com maior espaço ocupado. Através de um programa, 
# baixado da Internet, ele conseguiu gerar o seguinte arquivo, chamado "usuarios.txt":
#alexandre       456123789
#anderson        1245698456
#antonio         123456456
#carlos          91257581
#cesar           987458
#rosemary        789456125
#Neste arquivo, o nome do usuário possui 15 caracteres. A partir deste arquivo, você deve criar um programa que gere um relatório, chamado 
# "relatório.txt", no seguinte formato:
#O arquivo de entrada deve ser lido uma única vez, e os dados armazenados em memória, caso sejam necessários, de forma a agilizar a execução do programa. 
# A conversão da espaço ocupado em disco, de bytes para megabytes deverá ser feita através de uma função separada, que será chamada pelo programa principal. 
# O cálculo do percentual de uso também deverá ser feito através de uma função, que será chamada pelo programa principal.

with open('usuarios.txt') as arquivo:
    linhas = arquivo.read().splitlines()
    arquivo.close()

def organizaNomes(lista):
    listaNome = []
    for i in range(len(lista)):
        listaNome.append(lista[i][0:14].rstrip())
    return listaNome

def OrganizaTamanhoConsumido(lista):
    listaConsumo = []
    for i in range(len(lista)):
        listaConsumo.append(int(lista[i][15:len(lista[i])]))
    return listaConsumo

def ByteMega(lista):
    listaEmMega = []
    for i in range(len(lista)):
        listaEmMega.append(round(int(lista[i])/1048576,2))
    return listaEmMega

def calculaPorcetagem(lista):
    percentuais = []
    valorTotal = sum(lista)
    for i in range(len(lista)):
        percentuais.append(round((lista[i]/valorTotal)*100,2))
    return percentuais

def calculaEspacoMedio(lista):
    espacoMedio = round(sum(lista)/len(lista),2)
    return espacoMedio

def criaRelatorio(nomes, consumoMega, percentuais):
    if len(nomes) == len(consumoMega) == len(percentuais):
        open('relatorio.txt','a')
        arquivo = open('relatorio.txt','w')
        for i in range(len(nomes)):
            arquivo.write(str(i)+' '+str(nomes[i])+' '+str(consumoMega[i])+'MB '+str(percentuais[i])+'%'+'\n')
        totalConsumo = sum(consumoMega)
        consumoMedio = calculaEspacoMedio(consumoMega)
        arquivo.write('Consumo Total: '+str(totalConsumo)+'\n'+'Consumo Medio: '+str(consumoMedio)+'\n')
        arquivo.close()

    else:
        print('Quantidade de Usuarios e Dados Não Conferem.')

nomes = organizaNomes(linhas)
consumos = OrganizaTamanhoConsumido(linhas)
consumoMega = ByteMega(consumos)
percentuais = calculaPorcetagem(consumoMega)
criaRelatorio(nomes,consumoMega,percentuais)
