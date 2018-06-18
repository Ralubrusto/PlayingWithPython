# Abrindo e fechando arquivos
# 'w' sobrescreve
# 'a' 

# arquivo = open('teste.txt', 'a') 
# arquivo.write('\nHEY HEY HEY')
# arquivo.close()

arquivo = open('teste.txt', 'r') 
x = arquivo.readline()
arquivo.close()
print(x)
