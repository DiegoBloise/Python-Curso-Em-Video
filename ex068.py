from random import randint
vit = 0
print('-='*20)
print('Vamos jogar PAR ou ÍMPAR')
print('-='*20)
while True:
    jogada = input('Você quer PAR ou ÍMPAR? [P/I]: ').upper()
    nj = int(input('Escolha um número de 1 até 10: '))
    npc = randint(1, 10)
    print('-='*20)
    print(f'O computador jogou {npc} e você jogou {nj}.')
    tot = nj + npc
    print(f'Total de {tot}, ', end='')
    if tot % 2 == 0:
        print('\033[33mDEU PAR!\033[m')
    else:
        print('\033[33mDEU ÍMPAR!\033[m')
    if tot % 2 == 0 and jogada == 'P' or tot % 2 == 1 and jogada == 'I':
        print('\033[32mVocê Ganhou!\033[m')
        vit += 1
        print('-='*20)
    else:
        print('\033[31mVocê Perdeu!\033[m')
        print('-='*20)
        break
print()
print('\033[1;34m')
print('{:=^40}'.format(' Fim de Jogo '))
print('{:^40}'.format(f'Total de Vitórias Consecutivas: {vit}'))
print('='*40)
print('\033[m')
print()


'''
Faça um programa que jogue PAR ou ÍMPAR com o computador.
O jogo só sera interrompido quando o jogador PERDER,
mostrando o total de vitórias consecutivas que ele
conquistou no final do jogo.
'''
