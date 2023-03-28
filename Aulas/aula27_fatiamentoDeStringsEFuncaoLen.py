"""
    Fatiamento de strings
    012345678
    Olá mundo
   -987654321 

   Fatiamento [i:f:p] [::]

   Obs.: A função len retorna a quantidade de caracteres da string
"""

variavel = 'Olá mundo'
print(variavel[2:]) # irá mostrar do indice 2 até o final
print(variavel[0:5]) # irá mostrar do indice 0 até o indice 5
print(variavel[2:6]) # irá mostrar do indice 2 até o indice 6
print(variavel[-2:-6]) # irá mostrar do indice -2 até o indice -6
print(variavel[::2]) # irá mostrar toda a string pulando 2 caracteres