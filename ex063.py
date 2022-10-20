print('=== Sequência de Fibonacci ===')
t = int(input('Quantos termos quer mostrar?: '))
f1 = 0
f2 = 1
c = 2
print('\n{} -> {}'.format(f1, f2), end='')
while c != t:
    f3 = f1 + f2
    print(' -> {}'.format(f3), end='')
    f1 = f2
    f2 = f3
    c += 1
print()


'''
Escreva um programa que leia um número n inteiro qualquer
e mostre na tela os n primeiros elementos de uma Sequência de Fibonacci.
Ex:
0 -> 1 -> 1 -> 2 -> 3 -> 5 -> 8
'''
