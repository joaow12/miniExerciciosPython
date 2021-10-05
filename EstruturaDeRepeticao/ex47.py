#Em uma competição de ginástica, cada atleta recebe votos de sete jurados. A melhor e a pior nota são eliminadas. 
# A sua nota fica sendo a média dos votos restantes. Você deve fazer um programa que receba o nome do ginasta e as notas dos sete jurados alcançadas 
# pelo atleta em sua apresentação e depois informe a sua média, conforme a descrição acima informada (retirar o melhor e o pior salto e depois calcular a média com 
# as notas restantes). As notas não são informados ordenadas.

notas = []
nomes = ["Primeira", "Segunda", "Terceira", "Quarta", "Quinta", "Sexta", "Sétima"]
nome = True

while nome != "":
    nome = input("Digite o nome do atleta: ")
    if nome == "":
        break
    else:
        for i in range(7):
            z = float(input('Digite a {0} nota: '.format(nomes[i])))
            notas.append(z)
            if i == 0:
                maior = z
                menor = z
            if z>maior:
                maior = z
            elif menor>z:
                menor = z
        
        print("\nAtleta: ", nome, "\n")
        for i in range(7):
            print('{0} nota: {1}'.format(nomes[i], notas[i]))
        print('\nMelhor nota: {0} m \nPior nota: {1} m'.format(maior, menor))
        print('Média: {0:.2f}'.format(((sum(notas)-maior)-menor)/5))