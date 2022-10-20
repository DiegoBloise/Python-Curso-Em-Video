n = int(input('Digite um número para ver sua tabuada:'))
print()
print('-='*10)
print('{:^20}'.format('Tabuada do {}'.format(n)))
print('-='*10)
for nums in range(1, 11):
    print('{:^20}'.format('{} x {:2} = {}'.format(n, nums, n*nums)))
print('-='*10, '\n')


'''
Refaça o desafio 009 mostrando a tabuada de um número
que o usuário escolher, só que agora utilizando um laço for.
'''
