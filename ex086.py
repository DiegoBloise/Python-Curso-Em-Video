matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for l in range(3):
    for c in range(3):
        matriz[l][c] = int(input(f'Digite um valor para posição [{l}, {c}]: '))

print()
print('   +--------------+')
for l in range(3):
    print(f' {l} |', end='')
    for c in range(3):
        print(f'{matriz[l][c]:^4}', end='')
        print('|', end='')
    print('\n   +--------------+')
print('     0    1    2\n')


'''
Crie um programa que crie uma matriz de dimensão 3x3
e preencha com valores lidos pelo teclado.

       -----------
    0 |   |   |   |
      |-----------|
    1 |   |   |   |
      |-----------|
    2 |   |   |   |
       ----------- 
        0   1   2

No final, mostre a matriz na tela,
com a formatação correta.
'''
