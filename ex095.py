jogador = {}
jogadores = []
gols = []
total = partidas = 0

while True:
    jogador['Nome'] = str(input('Nome do jogador: '))

    partidas = int(input(f'Quantas partidas {jogador["Nome"]} jogou?: '))
    for c in range(partidas):
        gols.append(int(input(f'Quantos gols na {c+1}ª partida?: ')))
    jogador['Gols'] = gols[:]
    #jogador['Total'] = sum(gols)
    for v in gols:
        total += v
    jogador['Total'] = total
        
    jogadores.append(jogador.copy())
    jogador.clear()
    gols.clear()
    total = 0

    while True:
        resp = str(input('Quer continuar? [S/N]: ')).upper()
        if resp in 'SN':
            break
        print('Entrada inválida! Tente novamente...')

    if resp == 'N':
        break

print('-='*30)
print('''-----------------------------------------------
 COD  NOME               GOLS            TOTAL
-----------------------------------------------''')
for c, v in enumerate(jogadores):
    print(f'{c:>4}  ', end='')
    print(f'{v["Nome"]:<19}', end='')
    print(f'{str(v["Gols"]):<16}', end='')
    print(f'{v["Total"]}')
print('-'*47)

while True:
    cod = int(input('Mostrar dados de qual jogador? (999 para finalizar): '))
    if cod == 999:
        break
    elif cod not in range(len(jogadores)):
        print(f'ERRO! Não existe jogador com código {cod}! Tente novamente...')
    else:
        print(f'\n-- Levantamento do jogador {jogadores[cod]["Nome"]}:')
        for c, v in enumerate(jogadores[cod]["Gols"]):
            print(f'    => Na {c+1}ª partida, fez {v} gols.')
    print('-'*47)
print('\n<< VOLTE SEMPRE >>')


'''
Aprimore o desafio 093 para que ele funcione com vários jogadores, incluindo
um sistema de visualização de detalhes de aproveitamento de cada jogador.
'''