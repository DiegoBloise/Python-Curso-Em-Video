print('-'*45)
print('{:^45}'.format('Celsius para Fahrenheit'))
print('-'*45)
tc = float(input('Digite a temperatura em graus Celsius: '))
tf = (tc * 1.8) + 32
print('\nA temperatura de {:.0f}ºC equivale a {:.0f}ºF'.format(tc, tf))
print('-'*45)
print('{:^45}'.format('Fahrenheit para Celsius'))
print('-'*45)
tf = float(input('Digite a temperatura em graus Fahrenheit: '))
tc = (tf - 32) / 1.8
print('\nA temperatura de {:.0f}ºF equivale a {:.0f}ºC'.format(tf, tc))


'''
Escreva um programa que converta uma temperatura digitada
em graus Celsius e converta para graus Fahrenheit.
'''
