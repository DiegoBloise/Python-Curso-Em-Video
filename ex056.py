media = 0
hmv = 0
nomeh = 0
quantm = 0
for p in range(1, 5):
    nome = str(input('\nNome da {}ª pessoa: '.format(p)))
    idade = int(input('Idade da {}ª pessoa: '.format(p)))
    sexo = int(input('''Qual o sexo da {} pessoa?
[1]MASCULINO  [2]FEMININO

OPÇÃO: '''.format(p)))
    media += idade
    if sexo == 1 and idade > hmv:
        hmv = idade
        nomeh = nome
    if sexo == 2 and idade < 20:
        quantm += 1
print('\nMédia de idade do grupo: {:.0f} anos'.format(media / 4))
print('Nome do homem mais velho: {} ({} anos)'.format(nomeh, hmv))
print('Mulheres com menos de 20 anos: {}'.format(quantm))


'''
Desenvolva um programa que leia o nome, idade e sexo de
quatro pessoas. No final do programa mostre:
-A média da idade do grupo.
-Qual é o nome do homem mais velho.
-Quantas mulheres tem menos de 20 anos.
'''
