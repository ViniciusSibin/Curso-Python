"""
    Faça um programa que pergunte a hora ao usuário e, baseando-se no horário descrito, exiba a saudação apropriada. Ex Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-24.
"""
entrada = input('Digite uma hora no formato 0-24: ')

print('Método 1')
if entrada.isdigit():
    hora = int(entrada)
    if hora <= 11:
        print('Bom dia, seja muito bem vindo(a) ao sistema.')
    elif hora <= 18:
        print('Boa tarde, seja muito bem vindo(a) ao sistema.')
    elif hora <=23:
        print('Boa noite, seja muito bem vindo(a) ao sistema.')
    else:
        print('Não foi digitado a hora como pedido!!!')
else:
    print('Não foi digitado a hora como pedido!!!')

# OU 

print('\n\nMétodo 2')
try:
    hora = int(entrada)
    if hora <= 11:
        print('Bom dia, seja muito bem vindo(a) ao sistema.')
    elif hora <= 18:
        print('Boa tarde, seja muito bem vindo(a) ao sistema.')
    elif hora <=23:
        print('Boa noite, seja muito bem vindo(a) ao sistema.')
    else:
        print('Não foi digitado a hora como pedido!!!')
except:
    print('Não foi digitado a hora como pedido!!!')
