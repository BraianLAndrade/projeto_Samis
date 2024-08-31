'''
Loop for
loop = Estrutura de repetição.
For =  é uma dessas estruturas

C ou java
for(int i = 0; i < 10; i++){
    //execução do loop
}

# pynton
for item in interavel:
    //execução do loop

Utilizamos loops para iterar sobre sequencias ou sobre valores iteraveis.
--iterar cada um dos caracteres de uma string

EX:
-String
     nome = 'Braian'
-Lista
    lista = [1,2,3,4]
Range
    numeros = range(1,10)

 # Exemplo de for 1 (interaveis e iterando em uma string)
nome = 'harry Potter'
lista = [1, 3, 5,7,9]
numeros =  range(1, 10) # Temos que transformar em uma lista

for letra in nome:
    print(letra)

# Exemplo de for 2 ( iterando sobre uma lista)

for numero in lista:
    print(numero)

# Exemplo de for 3 ( interando sobre um range )
# Range valor inicial e valor fina - OBS o valor final não é incluido.
for numero in range(1, 10):
    print(numero) # 1,2,3,4,5,6,7,8 e 9.


# Enumerate
for indice, letra in enumerate(nome):
    print(nome[indice])
h
a
r
r
y

noeme =  'Braian lourenço'
for letra in nome:
    print(letra, end=' ')
Braian lourenço # sem pular as linhas como foi mostrado acima


for indice, letra in enumerate(nome):
    print(letra)
# Executa da mesma forma

for _, letra in enumerate(nome): #underline descarta o uso do indice e deixa so o do valor. ( 0, 'B',) normal com underline ( , 'B')
     print(letra)
Quando nao precisamos de um valor podemos descartar utilizando o underline


for valor in enumerate(nome):
    print(valor)

(0, 'h')
(1, 'a')
(2, 'r')
(3, 'r')
(4, 'y')

qtd = int(input('quantas vezes este loop deve rodar?'))

for n in range(1, qtd+1): # Para o numero no range até a quantidade imprima.
    print(f'imprimindo{n}')


    qtd = int(input('quantas vezes este loop deve rodar?'))
soma = 0
for n in range(1, qtd+1): # Para o numero no range até a quantidade imprima.
    num= int(input(f'Informe o {n}/{qtd} valor:'))
    soma = soma + num
print(f' A soma é {soma}')

quantas vezes este loop deve rodar?3
Informe o 1/3 valor:3
Informe o 2/3 valor:4
Informe o 3/3 valor:2
 A soma é 9

 nome = 'braian'
nome + 'lourenço'
print(nome + ' lourenço')
# Concatenação de string

A / é um caractere de scape,


'''

# Exemplo de for 1 (interaveis e iterando em uma string)
nome = 'harry Potter'
lista = [1, 3, 5,7,9]
numeros =  range(1, 10) # Temos que transformar em uma lista

# original: U+1F601
# modificado: U0001F601 - No lugar do mais coloquei 3 zeros

emoji = 'U0001F601'

for num in range(1, 11):
    print('\U0001F601' * num)

for _ in range(3):
    for num in range(1, 11):
        print('\U0001F601' * num)

emoji = '\U0001F468'

for _ in range(1,11):
    print('\U0001F468' * _)

emoji1= '\U0001F48F'
for casal in range(1,3):
    print('\U0001F48F' * casal)


