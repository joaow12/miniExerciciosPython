#Embaralha palavra. Construa uma função que receba uma string como parâmetro e devolva outra string com os carateres embaralhados. 
# Por exemplo: se função receber a palavra python, pode retornar npthyo, ophtyn ou qualquer outra combinação possível, de forma aleatória. 
# Padronize em sua função que todos os caracteres serão devolvidos em caixa alta ou caixa baixa, independentemente de como foram digitados.
import random

def embaralhar(texto):
    texto = texto.upper()
    embaralha = random.sample(texto, len(texto))
    a = ''.join(embaralha)
    print('A palavra {0} embaralhada fica {1}'.format(texto,a))

t = input("Digite algo que você deseje embaralhar: ")

embaralhar(t)
