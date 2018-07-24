# Princípios básicos de strings

# São definidas entre aspas
word1 = "Essa é uma string"
print(word1)

# Podem ser usadas aspas simples ou duplas
word2 = 'Essa também é uma string'
print(word2)

# Ou até mesmo aspas triplas. Nesse caso se trata de uma string multilinha
text = '''
Me casei com a mulher Certa
Só não sabia 
que seu primeiro nome era Sempre..

                            Veríssimo
'''
print(text)

''' Aspas triplas também servem para adicionar comentários em várias linhas. 
Essas linhas não serão consideradas pelo interpretador'''

# A escolha de aspas simples ou duplas fica a cargo do usuário.
# O segredo de uma em relação a outra é que aspas duplas escapam aspas simples, e vice versa

phrase1 = 'Percebe-se que nosso "inverno" chegou...'
print(phrase1)
phrase2 = "Hehehe 'só que não' :P"
print(phrase2)
