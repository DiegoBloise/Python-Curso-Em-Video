from math import sqrt
co = float(input('Digite o valor do cateto oposto: '))
ca = float(input('Digite o valor do cateto adjacente: '))
hp = sqrt(co*co + ca*ca)
print('A hipotenusa mede: {:.1f}'.format(hp))


'''
Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente
de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.
'''
