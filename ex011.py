lar = float(input('Digite a largura da parede em metros: '))
alt = float(input('Digite a altura da parede em metros: '))
area = lar * alt
tint = area / 2
print('''Para pintar uma parede com área de {:.2f}m²
Será necessário {:.2f} litros de tinta!'''.format(area, tint))


'''
Faça um programa que leia a largura e a altura de uma parede em metros,
calcule a sua área e a quantidade de tinta necessária para pintá-la,
sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.
'''
