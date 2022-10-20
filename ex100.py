from random import randint
from time import sleep

def sorteia(lista):
    print('Sorteando Números...')
    for n in range(5):
        lista.append(randint(1, 10))
        sleep(1)
        print(f'{lista[n]}...', end='', flush=True)


def somaPar(lista):
    somaPares = 0
    print('\nValores pares encontrados: ')
    for n in lista:
        if n % 2 == 0:
            somaPares += n
            sleep(1)
            print(f'{n}...', end='', flush=True)
    print('\nSoma de todos os valores pares: ')
    sleep(1)
    print(somaPares, flush=True)


nums = []
pares = []

sorteia(nums)
somaPar(nums)


'''
Faça um programa que tenha uma lista chamada números e duas funçoẽs
chamadas sorteia() e somaPar(). A primeira função vai sortear 5 números
e vai colocá-los dentro da lista e a segunda função vai mostrar a soma
entre todos os valores PARES sorteados pela função anterior. 
'''