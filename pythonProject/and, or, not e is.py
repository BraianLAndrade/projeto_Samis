'''
estruturas lógicas

Operadores unarios:
    ex: not
Operadores binarios:
    ex and, or, is
Para o and ambos os valores precisam ser True
Para o or um ou outro valor precisa ser True
Para o nor o valor do booleano é invertido , ou seja se for True vira false e se for False vira True

'''

ativo = True
logado = False

if ativo and logado:
    print('bem vindo usuario ao sistema')
else:
    print('voce precisa ativar sua conta, por favor nao seja burro!')


if ativo or logado:
    print('bem vindo usuario ao sistema')
else:
    print('voce precisa atiavar sua conta, por favor nao seja burro!')


# se não estiver ativo faça o que o print diz
if not ativo:
    print('voce precisa ativar sua conta rapaizinho ')
else:
    print('bem vindo usuario')




