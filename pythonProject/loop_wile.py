'''
Loop While

while expressão_booleana:
    // execução do loop

o bloco do while será reperido enquanto a expressão boleana for verdadeira.

Expressão booleana é toda expressão onde o resultado é verdadeiro ou falso.

EX:
num = 5
num < 5
False

num < 10
True

EXEMPLO 1

numero = 1

while numero < 10:
    print(numero)
    numero = numero +1

# OBS : em um loop while é importante que cuidemos do critério de parada. para não causar loop infinito;


# EXEMPLO 2

resposta = ' '
while resposta != 'sim':
    resposta = input('já acabou Jessica?:')

'''




'''
SAINDO DO LOOP COM BREAK 

Funciona da mesma for que nas linguagens C ou Java. 

Utilizamos o break para sair de loops de maneira projetada/forçada:

'''

# Exemplo 1

for numero in range (1,11):
    if numero == 6:
        break
    else:
        print(numero)
print('sai do loop')

# Exemplo 2

while True:
    comando = input("Digite 'sair'para sair:")
    if comando == 'sair':
        break


