#Criar uma calculadora onde faça as 4 operações básicas. + - * /

while True:
    numero1 = input('Digite o primeiro número da conta: ')
    operacao = input('Digite a operação desejada: soma(+), subtração(-), Multiplicação(*) ou Divisão(/): ')
    numero2 = input('Digite o segundo número da conta: ')
    flagNumero = None

    print('\n\n Para sair da calculadora digite SAIR a qualquer momento!!!\n\n')
    if numero1.lower() == 'sair' or numero2.lower() == 'sair' or operacao.lower() == 'sair':
        print('Fechando a calculadora!')
        break

    try:
        numero1 = float(numero1)
        numero2 = float(numero2)
        flagNumero = True
        
    except:
        flagNumero = None
        print('Um ou ambos os números digitados são inválidos!')
        continue


    if operacao == '+' or operacao.lower() == 'soma':
        operacao = '+'
        total = numero1 + numero2
    elif operacao == '-' or operacao.lower() == 'subtração' or operacao.lower() == 'subtraçao':
        operacao = '-'
        total = numero1 - numero2
    elif operacao == '*' or operacao.lower() == 'multiplicação' or operacao.lower() == 'multipliçao':
        operacao = '*'
        total = numero1 * numero2
    elif operacao == '/' or operacao.lower() == 'divisão' or operacao.lower() == 'divisao':
        operacao = '/'
        total = numero1 / numero2
    else:
        print('Operador digitado é inválido!\n')
        break
    
    print(f'{numero1}{operacao}{numero2} = {total:.2f}')