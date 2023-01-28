""" A função print por padrão pode receber vários argumentos separados por, 
e irá imprimir esses argumentos no terminal com espaço, e por padrão ela já 
vem com quebra de linha ao final da linha"""
print(12, 14, 16)
print("teste", "String", 16)


#o parâmetro sep="" altera o separador da função print
print("teste", "String", sep="->")

#o parâmetro end="" altera o final da linha do print, por padrão o final é o código de quebra de linha \r\n (Windows) ou \n (unix)
print("teste", "String", end="->")