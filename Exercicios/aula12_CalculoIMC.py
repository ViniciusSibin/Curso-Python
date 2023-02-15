nome = input('Digite seu nome: ')
altura = float(input('Digite sua altura: '))
peso = float(input('Digite seu peso: '))
imc = peso / (altura * altura)

#Nome da pessoa
# Pesa x quilos
# seu IMC é: 
#sua classificação é :

print('Nome: ' + nome)
print('Altura: ',altura, 'm')
print('Peso: ',peso, ' Kl')
print('Seu IMC é: ',imc)

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