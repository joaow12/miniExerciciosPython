#Em uma competição de salto em distância cada atleta tem direito a cinco saltos. No final da série de saltos de cada atleta, o melhor e o pior resultados são eliminados. 
# O seu resultado fica sendo a média dos três valores restantes. Você deve fazer um programa que receba o nome e as cinco distâncias alcançadas pelo atleta em seus saltos e 
# depois informe a média dos saltos conforme a descrição acima informada (retirar o melhor e o pior salto e depois calcular a média). Faça uso de uma lista para armazenar 
# os saltos. Os saltos são informados na ordem da execução, portanto não são ordenados. O programa deve ser encerrado quando não for informado o nome do atleta.

saltos = []
nomes = ["Primeiro", "Segundo", "Terceiro", "Quarto", "Quinto"]
nome = True

while nome != "":
    nome = input("Digite o nome do atleta: ")
    if nome == "":
        break
    else:
        for i in range(5):
            z = float(input('Digite o {0} salto: '.format(nomes[i])))
            saltos.append(z)
            if i == 0:
                maior = z
                menor = z
            if z>maior:
                maior = z
            elif menor>z:
                menor = z
        
        print("\nAtleta: ", nome, "\n")
        for i in range(5):
            print('{0} Salto: {1} m'.format(nomes[i], saltos[i]))
        print('\nMelhor salto: {0} m \nPior salto: {1} m'.format(maior, menor))
        print('Média dos demais saltos: {0:.2f} m'.format(((sum(saltos)-maior)-menor)/3))
        print('Resultado final: \n{0}: {1:.2f} m'.format(nome,((sum(saltos)-maior)-menor)/3))