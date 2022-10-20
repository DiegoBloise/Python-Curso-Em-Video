from time import sleep
import os
e = bool(input('''Pressione "Enter" para começar a contagem regressiva para a queima de fogos...'''))
os.system('clear')
for c in range(10, -1, -1):
    print('{}...'.format(c))
    sleep(1)
print('BUM!')


'''
Faça um programa que mostre na tela uma contagem regressiva
para o estouro de fogos de artifício, indo de 10 até 0,
com uma pausa de 1 segundo entre eles.
'''
