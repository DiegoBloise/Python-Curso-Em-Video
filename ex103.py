def ficha(jog='desconhecido', gol=0):
    print(f'O jogador {jog} fez {gol} gols.')

jogador = input('Nome do jogador: ')
gols = input('Número de gols: ')

if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0
if jogador.strip() == '':
    ficha(gol=gols)
else:
    ficha(jogador, gols)


'''
Faça um programa que tenha uma função chamada ficha(),
que receba dois parâmetros opcionais: o nome de um
jogador e quantos gols ele marcou.
O programa deverá ser capaz de mostrar a ficha do jogador,
mesmo que algum dado não tenha sido informado corretamente.
'''