from random import randint
npc = randint(0, 10)
nj = ''
t = 0
print('Em qual número estou pensando?')
while nj != npc:
    t += 1
    nj = int(input('Digite um número de 0 a 10: '))
    if nj != npc:
        print('Número errado! Tente novamente.')
print('Parabéns! Você acertou o número em {} tentativas.'.format(t))


'''
Melhore o jogo do DESAFIO 028 onde o computador
vai "pensar" em um número entre 0 e 10.
Só que agora o jogador vai tentar adivinhar até acertar,
mostrando no final quantos palpites foram necessários para vencer.
'''
