'''
Escopo de Variaveis

dois casos de scopo:
1- variaveis globais.
   - variaveis globais são reconhecidas, ou seja seu scopo compreende todo o programa.
2- variaveis locais.
    - variaveis locais são reconhecidas apenas no bloco onde foram declaradas, ou seja seu scopo esta limitado ao bloco onde foi declarada.

Para declarar variaveis em python fazemos:
nome_da_variavel = valor_da_variavel
EX : numero =42

python é uma linguagem de tipagem dinamica, isso significa que ao declararmos uma variave, nos nao colocamos o tipo de dado dela, este tipo é inferido ao
 atribuirmos  o valor a mesma.

Exemplo
int numero = 42

exemplo em java
int numero = 42

'''

# exemplo de variavél global

numero = 77 # variavél global
print(numero)
print(type(numero))

# Exemplo de variavél local

numero = 20

if numero > 10:
    novo = numero + 10
    print(novo)
#sempre abrimos um bloco colocando dois pontos :
#identação tem que ser de quatro espacço, cuidado com o tab.



