#Número por extenso. Escreva um programa que solicite ao usuário a digitação de um número até 99 e imprima-o na tela por extenso.

def converter_em_texto(num):
    y = ""
    dicionario = {
        0: 'zero', 1: 'um', 2: 'dois', 3: 'três', 4: 'quatro', 5: 'cinco',
        6: 'seis', 7: 'sete', 8: 'oito', 9: 'nove', 10: 'dez',
        11: 'onze', 12: 'doze', 13: 'treze', 14: 'quatorze', 15: 'quinze',
        16: 'dezesseis', 17: 'dezessete', 18: 'dezoito', 19: 'dezenove', 20: 'vinte',
        30: 'trinta', 40: 'quarenta', 50: 'cinquenta', 60: 'sessenta', 70: 'setenta',
        80: 'oitenta', 90: 'noventa',
    }

    if num>99 or num<0:
        print('Somente números de 0 a 99')

    if num< 20 or num% 10 == 0:
        return dicionario.get(num)

    decimal = num // 10 * 10
    unidade = num % 10
    extenso = f'{dicionario.get(decimal)} e {dicionario.get(unidade)}'
    return extenso

num = int(input("Digite um número: "))
numero_por_extenso = converter_em_texto(num)
print(numero_por_extenso)
