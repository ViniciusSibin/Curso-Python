"""
    Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva "Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande".
"""

nomeDigitado = len(input('Digite seu primeiro nome: '))


if nomeDigitado >= 1 and nomeDigitado <= 4:
    print(f'O nome digitado contém {nomeDigitado} letras, ele é curto.')
elif nomeDigitado >= 5 and nomeDigitado <= 6:
    print(f'O nome digitado contém {nomeDigitado} letras, ele é normal.')
elif nomeDigitado > 6:
    print(f'O nome digitado contém {nomeDigitado} letras, ele é muito grande.')
else:
    print('Digite algum nome por favor.')