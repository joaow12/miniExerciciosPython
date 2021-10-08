#Uma grande emissora de televisão quer fazer uma enquete entre os seus telespectadores para saber qual o melhor jogador após cada jogo. Para isto, 
# faz-se necessário o desenvolvimento de um programa, que será utilizado pelas telefonistas, para a computação dos votos. Sua equipe foi contratada para 
# desenvolver este programa. Para computar cada voto, a telefonista digitará um número, entre 1 e 23, 
# correspondente ao número da camisa do jogador. Um número de jogador igual zero, indica que a votação foi encerrada. Se um número inválido for digitado, 
# o programa deve ignorá-lo, mostrando uma breve mensagem de aviso, e voltando a pedir outro número. Após o final da votação, o programa deverá exibir:
#O total de votos computados;
#Os númeos e respectivos votos de todos os jogadores que receberam votos;
#O percentual de votos de cada um destes jogadores;
#O número do jogador escolhido como o melhor jogador da partida, juntamente com o número de votos e o percentual de votos dados a ele.
#Observe que os votos inválidos e o zero final não devem ser computados como votos. O resultado aparece ordenado pelo número do jogador. 
# O programa deve fazer uso de arrays. O programa deverá executar o cálculo do percentual de cada jogador através de uma função. Esta função receberá dois parâmetros: 
# o número de votos de um jogador e o total de votos. A função calculará o percentual e retornará o valor calculado.

voto = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
camisa = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22]
resp = True

while resp !=0:
    resp = int(input("Digite o número do jogador que você achou o melhor da partida: "))
    if resp == 0:
        break
    elif resp>0 and resp<=23:
        voto[resp-1] += 1
    elif resp>23:
        print("Número inválido (somente entre 1 e 23)")

print("\nResultado da votação: ")
print('Fora computados {0} votos'.format(sum(voto)))
print("Jogadores que receberam votos:")
for i in range(len(voto)):
    if voto[i]>0:
        porc = (voto[i]*100)/sum(voto)
        print('Camisa {0} = {1} votos / {2:.1f}%'.format(camisa.index(i)+1, voto[i],porc))
    