times = ('Internacional', 'São Paulo', 'Palmeiras', 'Flamengo', 'Atlético', 'Grêmio', 'Cruzeiro',
         'Santos', 'Fluminense', 'Corinthians', 'América-MG', 'Vitória', 'Bahia', 'Atlético-PR',
         'Botafogo', 'Vasco', 'Sport', 'Ceará', 'Chapecoense', 'Paraná')
print('-='*20)
print(f'\033[32mLista de times do Brasileirão:\033[33m {times}\033[m')
print('-='*20)
print(f'\033[32mOs 5 primeiros são:\033[33m {times[:5]}\033[m')
print('-='*20)
print(f'\033[32mOs 4 últimos são:\033[33m {times[-4:]}\033[m')
print('-='*20)
print(f'\033[32mTimes em ordem alfabética:\033[33m {sorted(times)}\033[m')
print('-='*20)
print(f"\033[32mO Chapecoense está na {(times.index('Chapecoense'))+1}ª posição\033[m")
print('-='*20)

'''
Crie uma tupla preenchida com os 20 primeiros colocados da tabela do
Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
A) Apenas os 5 primeiros colocados.
B) Os últimos 4 colocados da tabela.
C) Uma lista com os times em ordem alfabética.
D) Em que posição na tabela está o time da Chapecoense.
'''
