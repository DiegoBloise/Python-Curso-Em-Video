from random import randint
from time import sleep

palpites = []
temp = []

nj = int(input('\nQuantos jogos serão gerados?: '))

print(f"\n{' SORTEANDO {} JOGOS... ':=^50}\n".format(nj))

for j in range(nj):
    for n in range(6):
        while True:
            numero = randint(1, 61)
            if numero not in temp:
                temp.append(numero)
                break
    palpites.append(temp[:])
    temp.clear()

for c, p in enumerate(palpites):
    sleep(1)
    print(f'Jogo {c+1}: {sorted(p)}')

print(f"\n{' BOA SORTE ':=^50}\n")    


'''
Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
O programa vai perguntar quantos jogos serão gerados e vai sortear
6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.
'''