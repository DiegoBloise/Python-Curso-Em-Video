s = 0
tot = 0
for n in range(3, 500, 3):
    if n % 2 == 1:
        s += n
        tot += 1
print('''A soma de todos os números ímpares
multiplos de três, de 1 até 500 ({} valores)
é igual a: {}'''.format(tot, s))
print()


'''
Faça um programa que calcule a soma entre todos os
números ímpares que são multiplos de três e
que se encontram no intervalo de 1 até 500.
'''
