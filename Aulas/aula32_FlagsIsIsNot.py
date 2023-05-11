"""
    Flag (Bandeira) - Marcar um local
    None = Não valor
    is e is not = é ou não é (tipo, valor, identidade)
    id = identidade
"""
condicao = True
passou_no_if = None


if condicao:
    passou_no_if = True
    print('Entrou no if')
else:
    print('Não entrou no if')


if passou_no_if is None:
    print('Se não teve alteração na variável então não passou no if')

if passou_no_if is not None:
    print('Se a variável não for None é por que passou no if')


"""
    Quando usamos o is e o is not estamos comparando o tipo, o valor e a identidade da variável, por isso é recomendado sempre que seja possível utilizar.
"""