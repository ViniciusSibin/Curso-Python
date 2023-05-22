"""
    Operadores de atribuição
    = += -= *= /= //= **= %=
"""

contador = 10


contador += 1
print(f'Adição: 1 + 10 = {contador}')


contador -= 9
print(f'Subtração: 11 - 9 = {contador}')


contador *= 2
print(f'Multiplicação: 2 * 2 = {contador}')


contador /= 2
print(f'Divisão: 4 / 2 = {contador}')


contador //= 2
print(f'Divisão Inteira 2 // 2 = {contador}')

contador **= 2
print(f'Potencia: 1 ** 2 = {contador}')

contador %= 1
print(f'Resto da divisão: 1 % 1 = {contador}')