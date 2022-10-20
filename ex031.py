d = int(input('Qual a distância da viagem?:'))
if d <= 200:
    print('O preço da passagem será de R${:.2f}'.format((d*0.5)))
else:
    print('O preço da passagem será de R${:.2f}'.format((d*0.45)))


'''
Desenvolva um programa que pergunte a distância de uma viagem em Km.
Calcule o preço da passagem, cobrando R$0,50 por Km para viagens até 200Km
e R$0,45 para viagens mais longas.
'''
