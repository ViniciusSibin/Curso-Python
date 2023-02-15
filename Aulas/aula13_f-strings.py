nome = input('Digite seu nome: ')
altura = float(input('Digite sua altura: '))
peso = float(input('Digite seu peso: '))
imc = peso / (altura * altura)


string_1 = f'Nome: {nome}'
string_2 = f'Altura: {altura:.2f}m'
string_3 = f'Peso: {peso:.2f} Kl'
string_4 = f'Seu IMC é: {imc:.2f}'

print(string_1)
print(string_2)
print(string_3)
print(string_4)

if imc < 18.5:
    print('Sua classificação é: MAGREZA')
elif imc < 24.9:
    print('Sua classificação é: NORMAL')
elif imc < 29.9:
    print('Sua classificação é: SOBREPESO I')
elif imc < 39.9:
    print('Sua classificação é: OBESIDADE II')
else:
    print('Sua classificação é: OBESIDADE GRAVE III')

# MENOR QUE 18,5	MAGREZA	0
# ENTRE 18,5 E 24,9	NORMAL	0
# ENTRE 25,0 E 29,9	SOBREPESO	I
# ENTRE 30,0 E 39,9	OBESIDADE	II
# MAIOR QUE 40,0	OBESIDADE GRAVE	III 


