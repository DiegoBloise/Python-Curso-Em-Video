r1 = float(input('Comprimento da primeira reta: '))
r2 = float(input('Comprimento da segunda reta: '))
r3 = float(input('Comprimento da terceira reta: '))
if (r1+r2) > r3 and (r1+r3) > r2 and (r2+r3) > r1:
    print('As três retas podem formar um triângulo!')
else:
    print('As três retas NÃO podem formar um triângulo!')


'''
Desenvolva um programa que leia o comprimento de três retas
e diga ao usuário se elas podem ou não formar um triângulo.
'''
