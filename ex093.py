jogador = {}
gols = []
total = partidas = 0

jogador['Nome'] = str(input('Nome do jogador: '))

partidas = int(input(f'Quantas partidas {jogador["Nome"]} jogou?: '))
for c in range(partidas):
    gols.append(int(input(f'Quantos gols na {c+1}ª partida?: ')))

jogador['Gols'] = gols[:]

#jogador['Total'] = sum(gols)
for v in gols:
    total += v
jogador['Total'] = total

print('-='*30)
print(jogador)
print('-='*30)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}.')
print('-='*30)
print(f'O jogador {jogador["Nome"]} jogou {len(jogador["Gols"])} partidas.')
for c, v in enumerate(gols):
    print(f'    => Na {c+1}ª partida, fez {v} gols.')
print(f'Foi um total de {jogador["Total"]} gols.')


'''
Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa
vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado
em um dicionário, incluindo o total de gols feitos durante o campeonato.
'''