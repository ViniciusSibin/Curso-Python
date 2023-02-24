"""
    Operadores Lógicos
    and(e) or(ou) not(não)
    
    and - Todas as condições precisam ser verdadeira.
    
    Se qualquel valor for considerado falso a expressão inteira será avaliada naquele valor.

    São considerados falsy (que já foi visto) - 0, 0.0, '', False

    Também existe o tipo none que é utilizado para representar um não valor
"""

condicao1 = True
condicao2 = True

if condicao1 and condicao2:
    print('Operador AND --> As condições 1 e 2 são verdadeiras')


"""
    Operadores Lógicos  
    or - Qualquer expressão verdadeira avalia toda a expressão como verdadeira.

    Se qualquer valor for considerado verdadeiro, a expressão inteira será avaliada naquele valor.
    
    Se qualquel valor for considerado verdadeira a expressão será verdadeira.

    São considerados falsy (que já foi visto) - 0, 0.0, '', False

    Também existe o tipo none que é utilizado para representar um não valor
"""
condicao2 = False

if condicao1 or condicao2:
    print('Operador OR --> A condição 1 é verdadeira')

# exemplo 2

senha = input('Senha: ') or 'Sem senha'
print(senha)


"""
    Operadores lógicos
    not - usado para inverter expressões

    not True = False
    not False = True
"""

print(not True)  # False
print(not False)  # True


"""
    Operadores lógicos
    in e not in - Verifica se existe ou não um determinado valor em uma string

    Strings são iteráveis
    indice  -->  0 1 2 3 4 5 6 7 
    string  -->  v i n í c i u s
    inversa --> -8-7-6-5-4-3-2-1
"""
nome = 'vinícius'
if 'í' in nome:
    print(f'Tem a letra "í" na string: {nome}')
