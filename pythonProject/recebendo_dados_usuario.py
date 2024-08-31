"""
Rebendo dados usuario
todo dado recebendo via input é do tipo string
Em python string é tudo que estiver entre:
Aspas simples
Aspas duplas
Aspas simples triplas
Aspas duplas triplas
EX :
1- aspas simples -> 'Macaco louco'
2- aspas duplas -. "macaco louco"
3- aspas simples triplas-> '''macaco louco"""
 #4- aspas duplas triplas -> """macaco louco"""

# Entrada de dados
#print("qual o seu nome")
#nome =  input () # input -> entrada ou seja tem que adicionar a informação

# print("seja bem vindo %s" % nome ) # a procentagem indica que vou adicionar uma variavél e a %s que a cariavel adicionada ira substituir conforme o ex:

#print ("qual é a sua idade?")
#idade = input ()

# print ("A %s tem %s anos" % (nome, idade))

# os exemplos acima são antigos, tem como fazer de uma forma mais moderna.

#maneira atualizada de fazer os comandos acima
# print (f"seja bem-vindo(a) {nome}")

# int(idade) -> CAST
# Cast é a conversão de um tipo de dado para outro

nome = input("qual o seu nome? ")

idade = input("qual a sua idade? ")

print (f"O {nome} tem {idade} anos")

print(f"{nome} nasceu em {2024 - int(idade)}")

