# O input é utilizado para coletar dados do usuário no terminal. 

nome = input('Qual o seu nome? ')

print(f'O seu nome é {nome}')

# O retorno do input sempre é uma STR, por isso para trabalhar com números tem que ser feito a conversão

numero_1 = input('Digite um número: ')
numero_2 = input('Digite outro número: ')

int_numero_1 = int(numero_1)
int_numero_2 = int(numero_2)

print(f'A soma dos números digitados é: {int_numero_1 + int_numero_2}')