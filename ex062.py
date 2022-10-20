termo = int(input('Primeiro termo da PA: '))
razao = int(input('Razão da PA: '))
termos = 10
tm = 0
while termos != 0:
    c = 0
    print('\n(', end='')
    while c < termos:
        print('{}, '.format(termo), end='')
        termo += razao
        c += 1
        tm += 1
    print('...)')
    termos = int(input('\nQuantos termos você que mostrar a mais?: '))
print('\nProgressão finalizada com {} termos exibidos.'.format(tm))


'''
Melhore o DESAFIO 061, perguntando para o usuário se ele quer
mostrar mais alguns termos. O programa encerra quando ele
disser que quer mostrar 0 termos.
'''
