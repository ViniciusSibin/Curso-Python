#if / elif      / else
#se / se não se / se não

entrada = input('Você quer "entrar" ou "sair" ?')

if entrada == 'entrar': #Se a condição for verdadeira executa a linha abaixo
    print('Você entrou no sistema')
elif entrada == 'sair': #executa se a primeira condição não for verdadeira mas essa sim
    print('Você saiu do sistema')
else: # executa se nenhuma condição for verdadeira
    print('Você digitou uma opção invalida')
