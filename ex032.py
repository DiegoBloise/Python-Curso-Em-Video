ano = int(input('Digite o ano:'))
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano é BISSEXTO')
else:
    print('O ano NÃO é BISSEXTO')


'''
Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO.
'''
