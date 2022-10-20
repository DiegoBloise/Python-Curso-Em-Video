from random import randint
n = randint(0, 5)
print('---Adivinhe o Número---')
r = int(input('Digite um número de 0 a 5:'))
if r == n:
    print('Parabéns! Você acertou o número!')
else:
    print('''Que pena, você errou o número!
O número era escolhido era {}'''.format(n))


'''
Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5
e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
O programa deverá escrever na tela se o usuário venceu ou perdeu.
'''
