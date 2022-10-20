alunos = []
tempAluno = []
tempNotas = []

while True:
    tempAluno.append(str(input('Nome: ')))
    for n in range(1, 3):
        tempNotas.append(float(input(f'Nota {n}: ')))
    tempAluno.append(tempNotas[:])
    alunos.append(tempAluno[:])
    tempAluno.clear()
    tempNotas.clear()
    resp = input('Quer Continuar? [S/n]: ').lower()
    if resp == 'n':
        break

print()

print('='*30)
print(f"{'Nº:':>5}{'NOME:':>7}{'MÉDIA:':>16}")
print('-'*30)
for n, a in enumerate(alunos):
    print(f'  {n:.<5}{a[0]:.<15}{(a[1][0] + a[1][1]) / 2:.>4.1f}')
print('='*30)

while True:
    verN = int(input('\nMostrar notas de qual aluno? (999 interrompe): '))
    if verN == 999:
        break
    else:
        print(f'\nNotas de {alunos[verN][0]} são: {alunos[verN][1]}')
print('\nFINALIZADO.')


'''
Crie um programa que leia nome e duas notas de vários alunos
e guarde tudo em uma lista composta. No final, mostre um boletim
contendo a média de cada um e permita que o usuário possa
mostrar as notas de cada aluno individualmente.
'''