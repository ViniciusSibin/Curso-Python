"""
    Iterando strings com while
"""

#O usuário deve escrever uma palavra, e para cada letra deve conter um * antes e depois

while True:
    palavra = input('Digite uma palavra para ser formatada:  ')
    novaPalavra = ''
    i = 0
    if palavra.lower() == 'sair':
        print('Obrigado por jogar!!!')
        break
    elif len(palavra) > 0 and palavra != '':
        while i < len(palavra):
            novaPalavra += '*' + palavra[i]
            i += 1
        novaPalavra += '*'
        print(novaPalavra)
    else:
        print('Por gentileza, escreva uma palavra, ou digite SAIR')
        continue
