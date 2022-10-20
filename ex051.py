termo = int(input("Digite o primeiro termo da PA: "))
razao = int(input("Digite a razão da PA: "))
print("\n({}".format(termo), end=', ')
for c in range(0, 9):
    if razao > 0:
        termo += razao
    elif razao < 0:
        termo = razao
    print(termo, end=', ')
print("...)")


'''
Desenvolva um programa que leia o primeiro termo e a razão
de uma PA (progressão aritmética). No final, mostre os 10
primeiros termos dessa progressão.
'''
