pessoas = []
dados = []
pesados = []
leves = []

while True:
    dados.append(str(input('Nome da pessoa: ')))
    dados.append(float(input('Peso da pessoa: ')))
    pessoas.append(dados[:])
    dados.clear()
    resp = input('Cadastrar mais pessoas? [S/N]: ').lower()
    if resp == 'n':
        break

for c, p in enumerate(pessoas):
    if c == 0:
        pesados.append(p)
        leves.append(p)
        continue
    if p[1] > pesados[0][1]:
        pesados.clear()
        pesados.append(p)
    elif p[1] == pesados[0][1]:
        pesados.append(p)
    elif p[1] < leves[0][1]:
        leves.clear()
        leves.append(p)
    elif p[1] == leves[0][1]:
        leves.append(p)

def info1(lista):
    for c, p in enumerate(lista):
        print(p[0], end='')
        if c == len(lista) -2:
            print(' e ', end='')
        elif c == len(lista) -1:
            print('.')
        else:
            print(', ', end='')

def info2(lista):
    for c, p in enumerate(lista):
        print(f'{p[0]} com {p[1]} Kg', end='')
        if c == len(lista) -2:
            print(' e ', end='')
        elif c == len(lista) -1:
            print('.')
        else:
            print(', ', end='')

print()
print('~='*30)
print(f'Foram cadastradas {len(pessoas)} pessoas:')
info1(pessoas)
print('~='*30)
print(f'Pessoa(s) mais pesada(s) cadastrada(s):')
info2(pesados)
print('~='*30)
print(f'Pessoa(s) mais leve(s) cadastrada(s):')
info2(leves)
print('~='*30)


'''
Faça um programa que leia o nome e peso de várias pessoas,
guardando tudo em uma lista. No final, mostre:
(A) Quantas pessoas foram cadastradas.
(B) Uma listagem com as pessoas mais pesadas.
(C) Uma listagem com as pessoas mais leves.
'''