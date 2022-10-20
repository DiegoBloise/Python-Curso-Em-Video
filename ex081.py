numeros = []
while True:
    numeros.append(int(input('Digite um número: ')))
    resp = input('Continuar? ')
    if resp in 'Nn':
        break
print(f'Foram digitados {len(numeros)} números,')
print(f'Sendo eles em ordem decrescente: {sorted(numeros, reverse=True)}')
if 5 in numeros:
    print(f'O valor 5 foi digitado e está na {numeros.index(5)}ª posição.')
else:
    print('O valor 5 não foi digitado.')


'''
Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, mostre:
A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista.
'''