from random import randint
from time import sleep
from os import system
cont = 1
pj = 0
ppc = 0
while cont == 1:
    system('clear')
    print('{:=^40}'.format(' JOKENPY '))
    print('''SELECIONE SUA JOGADA:
[0] PEDRA
[1] PAPEL
[2] TESOURA''')
    jj = int(input('OPÇÃO: '))
    jpc = randint(0, 2)
    jogadas = ['PEDRA', 'PAPEL', 'TESOURA']
    system('clear')
    print('Jo...')
    sleep(1)
    system('clear')
    print('Joken...')
    sleep(1)
    system('clear')
    print('JokenPy!')
    sleep(0.5)
    print('''{:=^40}
       COMPUTADOR:{}x{}:JOGADOR'''.format('PLACAR', ppc, pj))
    print('=' * 40)
    print('''Computador escolheu {}
Jogador escolheu {}\n'''.format(jogadas[jpc], jogadas[jj]))
    print('-' * 40)
    if jj == 0 and jpc == 2 or jj == 1 and jpc == 0 or jj == 2 and jpc == 1:
        print('JOGADOR VENCEU!')
        pj = pj + 1
    elif jj == jpc:
        print('EMPATE!')
    else:
        print('JOGADOR PERDEU!')
        ppc = ppc + 1
    print('-' * 40)
    cont = int(input('''
CONTINUAR?
[1] SIM   [2] NÃO
>>> '''))
system('clear')
print('{:-^40}'.format('FIM DE JOGO'))
print('''{:=^40}
       COMPUTADOR:{}x{}:JOGADOR'''.format('PLACAR FINAL', ppc, pj))
print('=' * 40)
print('\n' * 10)


'''
Crie um programa que faça o computador
jogar "Jokenpô" com você.
'''
