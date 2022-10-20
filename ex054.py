from datetime import date
menores = 0
maiores = 0
for c in range(1, 8):
    ano = int(input('Digite o {}º ano de nascimento: '.format(c)))
    idade = date.today().year - ano
    if idade < 18:
        menores += 1
    else:
        maiores += 1
print("Das {} pessoas analisadas, {} não atingiram a maioridade e {} já são maiores.".format(c, menores, maiores))


'''
Crie um programa que leia o ano de nascimento de sete pessoas.
No final, mostre quantas pessoas ainda não atingiram
a maioridade e quantas já são maiores.
'''
