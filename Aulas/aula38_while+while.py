"""
    Repetições
    while (enquanto)
    Executa uma ação enquanto uma ação for verdadeira.
    Loop infinito --> Quando um código não tem fim, executa constantemente. 
    break --> Quebra o laço e vai para o próximo bloco de código
    continue --> Corta o laço onde estiver e volta para o começo 
"""

qtd_linhas = 5
qtd_colunas = 5

linha = 1

while linha <= qtd_linhas:
    coluna = 1
    while coluna <= qtd_colunas:
        print(f'{linha=} {coluna=}')
        coluna += 1
    linha += 1
print('Acabou')