from random import randint

nums = (randint(1, 9), randint(1, 9), randint(1, 9), randint(1, 9), randint(1, 9))
print(f'Os valores sorteados foram: {nums}')
print(f'O maior valor sorteado foi {max(nums)}')
print(f'O menor valor sorteado foi {min(nums)}')


'''
Crie um programa que vai gerar cinco números aleatórios
e colocar em uma tupla.
Depois disso, mostre a listagem de números gerados e também
indique o menor e o maior valor que estão na tupla.
'''
