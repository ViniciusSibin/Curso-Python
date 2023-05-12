"""
    Faça um programa que peça ao usuário para digitar um número inteiro, informese este número é par ou ímpar. caso o usuário não digite um número inteiro informe que não não é um número inteiro.
"""

entrada = input('Digite um número inteiro: ')

print('Primeiro método')
if entrada.isdigit():
    numeroDigitado = int(entrada)
    if numeroDigitado % 2 == 0:
        print(f'O número {numeroDigitado} é PAR!')
    else:
        print(f'O número {numeroDigitado} é ÍMPAR!')
else:
    print('Não foi digitado um número inteiro')
# Do modo feito acima com if só é possível utilizar números inteiros.
############## OU ###################

print('\n\nSegundo método')
try:
    numeroDigitado = float(entrada)
    if numeroDigitado % 2 == 0:
        print(f'O número {numeroDigitado} é PAR!')
    else:
        print(f'O número {numeroDigitado} é ÍMPAR!')
except:
    print('Não foi digitado um número inteiro')

# Do modo feito acima além de ser possível utilizar ponto flutuante, posteriormente pode ser feito o tratamento do erro.