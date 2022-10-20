numeros = []
pares = []
impares = []
while True:
    numeros.append(int(input('Digite um valor: ')))
    resp = input('Continuar? [S/N]')
    if resp in 'Nn':
        break
for n in numeros:
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)
print('~'*40)
print(f'''Todos os valores digitados:
{numeros}''')
print('~'*40)
print(f'''Todos os valores pares digitados:
{pares}''')
print('~'*40)
print(f'''Todos os valores ímpares digitados:
{impares}''')
print('~'*40)


'''
Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, crie duas listas extras que vão conter apenas os
valores pares e os valores ímpares digitados, respectivamente.
Ao final, mostre o conteúdo das três listas geradas.
'''