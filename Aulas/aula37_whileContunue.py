"""
    Repetições
    while (enquanto)
    Executa uma ação enquanto uma ação for verdadeira.
    Loop infinito --> Quando um código não tem fim, executa constantemente. 
    break --> Quebra o laço e vai para o próximo bloco de código
    continue --> Corta o laço onde estiver e volta para o começo 
"""

contador = 0


#Contar de 0 a 100 mostrando somente os números pares
while contador <= 100:
    if contador % 2 == 0:
        print(contador)
    
    contador = contador + 1
    continue

print('Finalizado')