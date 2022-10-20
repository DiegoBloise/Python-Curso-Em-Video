km = int(input('Digite a velocidade do carro:'))
al = km-80
m = al*7
if km > 80:
    print('''O carro foi multado por ultrapassar {}Km acima do limite
de 80Km/h e deverá pagar R${},00 de multa.'''.format(al, m))
else:
    print('O carro está dentro do limite de 80Km/h.')


'''
Escreva um programa que leia a velocidade de um carro.
Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
A multa vai custar R$7,00 por cada Km acima do limite.
'''
