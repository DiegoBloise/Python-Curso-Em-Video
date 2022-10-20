n = int(input('Digite um número para ver seu fatorial: '))
tot = 1
print('{}! = '.format(n), end='')
while n >= 1:
    print('{}'.format(n), end='')
    if n > 1:
        print('x', end='')
    tot *= n
    n -= 1
print(' = {}'.format(tot))


'''
Faça um programa que leia um número qualquer e mostre seu fatorial.
Ex:
5! = 5x4x3x2x1 = 120
'''
