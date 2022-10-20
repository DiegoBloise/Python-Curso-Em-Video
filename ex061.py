termo = int(input('Primeiro termo da PA: '))
razao = int(input('Razão da PA: '))
c = 0
print('\n(', end='')
while c < 10:
    print('{}, '.format(termo), end='')
    termo += razao
    c += 1
print('...)')


'''
Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA,
mostrando os 10 primeiros termos da progressão usando a estrutura while.
'''
