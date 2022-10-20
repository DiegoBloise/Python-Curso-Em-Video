matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somaPares = somaColuna = 0
for l in range(3):
    for c in range(3):
        matriz[l][c] = int(input(f'Digite um valor para posição [{l}, {c}]: '))
        if matriz[l][c] % 2 == 0:
            somaPares += matriz[l][c]
        if matriz[l][c] == matriz[l][2]:
            somaColuna += matriz[l][2]  
print()
print('   +--------------+')
for l in range(3):
    print(f' {l} |', end='')
    for c in range(3):
        print(f'{matriz[l][c]:^4}', end='')
        print('|', end='')
    print('\n   +--------------+')
print('     0    1    2\n')

print(f'A soma dos valores pares é: {somaPares}')
print(f'A soma dos valores da terceira coluna é: {somaColuna}')
print(f'O maior valor da segunda linha é: {max(matriz[1])}')


'''
Aprimore o desafio anterior, mostrando no final:
(A) A soma de todos os valores pares digitados.
(B) A soma dos valores da terceira coluna.
(C) O maior valor da segunda linha.
'''