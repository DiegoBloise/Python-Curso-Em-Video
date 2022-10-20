from random import randint
from time import sleep
from operator import itemgetter

jogadores = {}
ranking = {}

for c in range(1, 5):
    jogadores[f'Jogador {c}'] = randint(1, 6)

print('\nValores Sorteados:')
for k,v in jogadores.items():
    sleep(1)
    print(f'    O {k} tirou {v}')
sleep(1)

ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
print('\nRanking dos Jogadores:')
for i, v in enumerate(ranking):
    sleep(1)
    print(f'    {i+1}º Lugar: {v[0]} com {v[1]}')



'''
Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
Guarde esses resultados em um dicionário. No final, coloque esse dicionário em ordem,
sabendo que o vencedor tirou o maior número no dado.
'''