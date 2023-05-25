"""
    Criar um script para verificar qual caractere apareceu mais vezes na frase.
"""
frase = 'O Python é uma linguagem de programação multiparadigma. Python foi criado por Guido van Rossum.aaaaaaaaaaaaaaaaawwwwwwwwwwwwwwwwwwwwwww'
i = 0
letra_final = ''
qtd_caracteres_final = 0

while i < len(frase):
    qtd_caracteres = frase.count(frase[i])

    if qtd_caracteres > qtd_caracteres_final:
        qtd_caracteres_final = qtd_caracteres
        letra_final = frase[i]
    elif qtd_caracteres == qtd_caracteres_final:
        if frase[i] not in letra_final:
            letra_final += ', ' + frase[i]

    i += 1
print(f'A letra que mais apareceu foi: {letra_final} por {qtd_caracteres_final} vezes!!!')