from random import randint
from time import sleep
lista = []

def maior(*num):
    print('-='*30)
    print('Analisando os valores informados...')
    sleep(0.7)
    for n in num:
        sleep(0.6)
        print(f'{n} ', end='', flush=True)
    sleep(1)
    print(f'\nForam informados {len(num)} valores ao todo;')
    sleep(1)
    print('O maior valor informado foi ', end='')
    if len(num) > 0:
        print(max(num))
    else:
        print(0)
    sleep(1)

for c in range(5):
    for n in range(randint(0, 10)):
        lista.append(randint(0, 10))
    maior(*lista)
    lista.clear()


'''
Faça um programa que tenha uma função chamada maior(),
que receba vários parâmetros com valores inteiros.

Seu programa tem que analisar todos os valores
e dizer qual deles é o maior.
'''