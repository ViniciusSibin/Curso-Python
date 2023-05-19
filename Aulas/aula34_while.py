"""
    Repetições
    while (enquanto)
    Executa uma ação enquanto uma ação for verdadeira.
    Loop infinito --> Quando um código não tem fim, executa constantemente. 
"""

condicao = True

while condicao:
    nome = input('Escreva alguma coisa: ')
    print(f'nome escrito: {nome}')

    if nome == "sair": #Enquanto o usuário não digitar sair, o loop não para de executar.
        break
