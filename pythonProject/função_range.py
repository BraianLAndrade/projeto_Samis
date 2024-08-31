'''
Ranges
. precisamos conhecer o loop for para usar os ranges
. precisamos conhecer o range para trabalhar melhor com loops for

ranges são utilizados para gera sequencias numericas não de forma aleatória, mas sim de maneira especificada.

formas gerais:

forma 1
range(valor_de_parada)

OBS: valor de parada não inclusive, (inicio padrão 0, e passo de 1 em 1)

Ex: forma 1
# forma 1
for num in range (11):
    print(num)

#forma 2
range (valor_de_inicio, valor_de_parada)

OBS: valor de parada não inclusive, (inicio especificado pelo usuario , e passo de 1 em 1)
# forma 2
for num in range(5,11):
    print(num)

#forma 3
Range (valor_de_inicio, valor_de_parada, passo )
OBS: valor de parada não inclusive, (inicio especificado pelo usuario , e passo especificado pelo usuario)

# forma 3
for num in range(1,10,2):
    print(num) # = 1,3,5,7,9

#forma 4 (inversa
Range (valor_de_inicio, valor_de_parada, passo )
OBS: valor de parada não inclusive, (inicio especificado pelo usuario , e passo especificado pelo usuario)

# forma 4
for num in range(10,0,-1):
    print(num)

    
'''


# forma 4
for num in range(10,0,-1):
    print(num)


