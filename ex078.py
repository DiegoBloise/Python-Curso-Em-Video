valores = []
for v in range(1, 6):
    valores.append(input(f'Digite o {v}º valor: '))
print(f'O maior valor digitado foi {max(valores)} na posição {valores.index(max(valores))}')
print(f'O menor valor digitado foi {min(valores)} na posição {valores.index(min(valores))}')


'''
Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
No final, mostre qual foi o maior e o menor valor digitado
e as suas respectivas posições na lista.
'''