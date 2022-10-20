n = 0
print('=== Detector de Números Primos ===')
num = int(input('Qual o número?: '))
for c in range(1, num + 1):
    if num % c == 0:
        n += 1
if n == 2:
    print('\n{} É um número primo.'.format(num))
else:
    print('\n{} NÃO um número primo.'.format(num))


'''
Faça um programa que leia um número inteiro e
diga se ele é ou não um número primo.
'''
