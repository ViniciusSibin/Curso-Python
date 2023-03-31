"""
    Introdução ao try/except
    try --> tentar executar o código
    except --> ocorreu algum erro ao tentar executar
"""

numero_str = input('Irei dobrar o número que você digitar: ')

try: # o Try sempre irá executar o código até encontrar o erro.
    numero_float = float(numero_str)
    print('Digitado: ', numero_str)
    print('convertido: ', numero_float)
    print(f'O dobro de {numero_str} é {numero_float * 2:.2f}')
except:
    print('Não foi digitado um número.')