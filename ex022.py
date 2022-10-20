nome0 = str(input('Digite seu nome completo:')).strip()
print(nome0.upper())
print(nome0.lower())
nome1 = nome0.split()
print('O nome completo tem {} letras'.format(len(nome0) - nome0.count(' ')))
print('O primeiro nome é {} e tem {} letras'.format(nome1[0], len(nome1[0])))


'''
Crie um programa que leia o nome completo de uma pessoa e mostre:
O nome com todas as letras maiúsculas
O nome com todas as letras minúsculas
Quantas letras ao todo (sem considerar os espaços)
Quantas letras tem o primeiro nome
'''
