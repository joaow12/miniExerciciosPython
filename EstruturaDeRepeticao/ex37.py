#Uma academia deseja fazer um senso entre seus clientes para descobrir o mais alto, o mais baixo, a mais gordo e o mais magro, para isto você deve fazer um programa 
# que pergunte a cada um dos clientes da academia seu código, sua altura e seu peso. O final da digitação de dados deve ser dada quando o usuário digitar 0 (zero) no 
# campo código. Ao encerrar o programa também deve ser informados os códigos e valores do clente mais alto, do mais baixo, do mais gordo e do mais magro, além da média 
# das alturas e dos pesos dos clientes

resp = 1
mAlt = 0
mPeso = 0
cont = 1

while resp != 0:
    cod = int(input("Digite o código: "))
    if cod == 0:
        break

    else:
        alt = float(input("Digite sua altura: "))
        peso = float(input("Digite o seu peso: "))

        mAlt += alt
        mPeso += peso

        if cont == 1:
            maiorP = peso
            menorP = peso
            maiorA = alt
            menorA = alt

        if peso>maiorP:
            maiorP = peso
            maiorCod = cod
            maiorAlt = alt

        elif peso<menorP:
            menorP = peso
            menorCod = cod
            menorAlt = alt

        if alt>maiorA:
            maiorA = alt
            maiorCodA = cod
            maiorPeso = peso

        elif alt<menorA:
            menorA = alt
            menorCodA = cod
            menorPeso = peso
        
        cont += 1

print('DADOS DA ACADEMIA')
print('Menor peso: \nCódigo: {0} \nAltura: {1} \nPeso: {2}'.format(menorCod, menorAlt, menorP))
print('Maior peso: \nCódigo: {0} \nAltura: {1} \nPeso: {2}'.format(maiorCod, maiorAlt, maiorP))
print('Maior Altura: \nCódigo: {0} \nAltura: {1} \nPeso: {2}'.format(maiorCodA, maiorA, maiorPeso))
print('Menor Altura :\nCódigo: {0} \nAltura: {1} \nPeso: {2}'.format(menorCodA, menorA, menorPeso))
print('Média de altura: {0:.2f} \nMédia de peso: {1:.2f}'.format(mAlt/cont, mPeso/cont))
