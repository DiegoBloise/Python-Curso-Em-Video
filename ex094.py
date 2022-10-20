dados = {}
pessoas = []
mulheres = []
soma = 0

while True:
    dados['Nome'] = str(input('Nome: '))
    while True:
        dados['Sexo'] = str(input('Sexo [M/F]: ')).upper()
        if dados['Sexo'] in 'MF':
            break
        print('Entrada inválida! Tente novamente...')
    if dados['Sexo'] == 'F':
        mulheres.append(dados['Nome'])
    dados['Idade'] = int(input('Idade: '))
    pessoas.append(dados.copy())
    while True:
        resp = str(input('Quer continuar? [S/N]: ')).upper()
        if resp in 'SN':
            break
        print('Entrada inválida! Tente novamente...')
    if resp == 'N':
        break

for p in range(len(pessoas)):
    soma += pessoas[p]['Idade']
media = soma / len(pessoas)

print('-='*40)
print(f'- Foram cadastradas {len(pessoas)} pessoas.')
print(f'- A média de idade é de {media:.1f} anos.')
print('- As mulheres cadastradas foram: ',end='')
for m in mulheres:
    print(m, end=' ')
print('\n')    
print('- Lista das pessoas que estão acima da média:')
for p in pessoas:
    if p['Idade'] > media:
        print()
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')

print('\n<< ENCERRADO >>')


'''
Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados
de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas
B) A média de idade do grupo
C) Uma lista com todas as mulheres
D) Uma lista com todas as pessoas com idade acima da média
'''