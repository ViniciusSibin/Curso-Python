"""
    while/else

    Se o while for executando até o final (sem interrupções) ai sim é executado o else.
"""
string = 'Valor qualquer'

i = 0
while i < len(string):
    letra = string[i]

    if letra == ' ':
        break

    print(letra)
    i += 1
else:
    print('Não encontrei um espaço na string')
print('Fora do while')