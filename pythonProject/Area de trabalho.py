'''numero =  int(input('Digite o numero:'))

if numero % 2 == 0:
    print('numero par')
    if numero %4 ==0:
        print(f'{numero} é multiplo de 4')
    else:
        print('numero impar')

for num in range(1, 10):
    if (num % 2 !=0):
        print(num)'''


'''idade = int(input('quanto anos vc tem:'))

if idade > 18:
    print(f'o garoto tem {idade} anos, portanto pode ser preso')
else:
    print('o garoto não pode ser preso')


nome =  input('qual é o seu nome? ')
print('que lega!')
idade1 = input('Qaul é a sua idade?')
print(f'Sendo assim a  {nome} nasceu em: {2024 - int(idade1)}')'''

'''def formulario(): # Toda função tem que estar entre parentese
    nome = (input('Qual é o seu nome?:'))
    idade = int(input('Qaul é a sua idade?:'))

    print(f'Sr(a) {nome} tem {idade} anos de idade')
    print('Proximo!')

formulario()
formulario()
formulario()'''

print( 'Sorteio do Rei do rio'. upper())
def sortecerta():
    emoji = 1
    numero = (int(input('Digite seu numero da sorte: ')))
    if numero  == 13:
        print('achamos o rei do rio')
    else:
        print('Não foi desta vez, tente outro numero' '\U0001F601' * emoji )
        while sortecerta():
            if sortecerta() == 13:
                break

sortecerta()




