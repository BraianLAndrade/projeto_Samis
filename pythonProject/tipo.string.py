"""
Tipo string
Em python um dado é considerado do tipo string sempre que estiver entre aspas simples.
EX - 'uma sting', 'a', '212', 'True'.
Sempre que estiver entre aspas duplas.
"string", "233", "a"...
EStiver entre aspas simples tripla. EX: ''' ola''', '''1234''', '''4. 23'''

nome = 'braian'
print(nome)
print(type (nome))

nome = "honye'house"
print(nome)
print(type(nome))

nome = 'naruto \n uzunaky'
print(nome)
print (type(nome))

print(nome.split())
o split traz algo em lista.
['braian', 'npofbra']



nome = 'braian npofbra'
print(nome[0:7])
imprime o nome até a quantidade de letras defindas[0:7] por exemplo.

print(nome.upper())
deixa as letras no maiusculo

nome = 'braian npofbra'
print(nome[7:14])
print(nome[0:7]) # chamamos esta operação de slice de string
print(nome.split()[0])
#    [ 0,     1]

print(nome[::-1]) # comece do 1 elemento com dois pontos e vai até o ultimo elemento mais dois pontos de traz para frente -1.
arbfopn naiarb # resultado da programação acima

print(nome.replace('b', 't'))
traian npoftra
replace é usado para substituir palavras conform vemos acima.

"""
#Estiver e, aspas duplas triplas. EX """olaa""", """ foi""", """123.3"""

nome = 'braian npofbra'

print(nome[::-1])
#arbfopn naiarb # resultado da programação acima

print(nome.replace('b', 't'))

texto =  'socarram me subino onibus em marrocos'
print(texto)
print(texto[::-1])
#Palindromo quando o inverso é a mesma coisa

inverso = 'Roma'
print(inverso)
print(inverso[::-1])

nome = 'carol \n '
print()