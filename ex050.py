tot = 0
for c in range(1, 7):
    n = int(input('Digite o {}º valor:'.format(c)))
    if n % 2 == 0:
        tot += n
print('Total da soma de todos os valores pares: {}'.format(tot))


'''
Desenvolva um programa que leia seis números inteiros e
mostre a soma apenas daqueles que forem pares.
Se o valor digitado for ímpar, desconsidere-o
'''
