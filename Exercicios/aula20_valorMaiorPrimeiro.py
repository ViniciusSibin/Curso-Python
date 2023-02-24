"""
    O usuário deve digitar 2 valores e deve aparecer na tela a frase primeiro_valor='2' é maior que o segundo_valor='1'
"""

primeiro_valor = input('Digite o primeiro valor: \n')
segundo_valor = input('Digite o segundo valor: \n')

if primeiro_valor >= segundo_valor:
    print(f'{primeiro_valor=} é maior ou igual ao {segundo_valor=}')
else:
    print(f'{segundo_valor=} é maior ou igual ao {primeiro_valor=}')
