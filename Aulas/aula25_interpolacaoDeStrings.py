"""
    Interpolação de strings
    s - string
    d e i - int
    f - float
    x e X - Hexadecimal (0123456789abcdef)
"""

nome = 'Vinicius'
preco = 500.7673
variavel = '%s, o valor é R$%.2f' % (nome, preco)
print(variavel)
print('O hexadecimal de %d é: %08x' % (300, 300))