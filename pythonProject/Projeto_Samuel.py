#Lobby do LOL


#invocadores
player1 = ('TOP')
player2 = ('MID')
player3 = ('Jungle')
player4 = ('ADC')
player5 = ('SUP')

# Rotas
campeostop = ['darius', 'Garen', 'trindamery', 'orn'. title()]
campeosmid = ['leblanc', 'arhi', 'syndra', 'zoe<3'. title()]
campeosjg = ['kayn','master', 'irven', 'fidlestick'. title()]
campeoessup = ['morgana','nautilos','lux_não_é_sup', ' nautilos'.title()]
campeoesadc = ['draven', 'lucian', 'jhin', 'jhinx', 'caitlyn'.title()]


def usando_for():
    for mid in range(1):
        (mid:=(input(f'o {player2}  deve declarar seu campeão:')))
        if mid != campeosmid:
            print(f'A sua lane será mid com {mid}.'.upper())
        else:
            print('Para delacar seu campeão digite o nome corretamente!')

    for top in range(1):
        (top:=(input(f'o {player1}  deve declarar seu campeão:')))
        if top != campeosmid:
            print(f'A sua lane será top com {top}.'.upper())
        else:
            print('Para delacar seu campeão digite o nome corretamente!')

    for jungle in range(1):
        (jungle:=(input(f'o {player3}  deve declarar seu campeão:')))
        if jungle != campeosmid:
            print(f'A sua lane será jungle com {jungle}.')
        else:
            print('Para delacar seu campeão digite o nome corretamente!')

    for sup in range(1):
        (sup:=(input(f'o {player5}  deve declarar seu campeão:')))
        if sup != campeosmid:
            print(f'A sua lane será sup com {sup}.')
        else:
            print('Para delacar seu campeão digite o nome corretamente!')

    for adc in range(1):
        (adc:=(input(f'o {player4}  deve declarar seu campeão:')))
        if adc != campeosmid:
            print(f'A sua lane será adc com {adc}.')
        else:
            print('Para delacar seu campeão digite o nome corretamente!')


def escolhalane ():
    if ( top:= (input(f'o {player1} deve escolher seu campeão {campeostop}: '))) != campeostop:
        print(f'sua lane será top com {top}')
    else:
        print('declares seu campeção, escreva como está')

    if ( mid:= (input(f'o {player2} deve escolher seu campeão {campeosmid}: '))) != campeostop:
        print(f'sua lane será top com {mid}')
    else:
        print('declares seu campeção, escreva como está')

    if ( jungle:= (input(f'o {player3} deve escolher seu campeão {campeosjg}: '))) != campeostop:
        print(f'sua lane será top com {jungle}')
    else:
        print('declares seu campeção, escreva como está')

    if ( sup:= (input(f'o {player5} deve escolher seu campeão {campeoessup}: '))) != campeostop:
        print(f'sua lane será top com {top}')
    else:
        print('declares seu campeção, escreva como está')

    if ( adc:= (input(f'o {player4} deve escolher seu campeão {campeoesadc}: '))) != campeostop:
        print(f'sua lane será top com {adc}')
    else:
        print('declares seu campeção, escreva como está')


    print('A partida começara em 30 segundos'.upper())

    for tempo in range (30,0,-1):
        print(tempo)


    if ( top:= (input(f'o {player1} deve escolher seu campeão {campeostop}: '))) != campeostop:
        print(f'sua lane será top com {top}')
    else:
        print('declares seu campeção, escreva como está')





usando_for()