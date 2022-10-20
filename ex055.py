peso = float(input("Digite o peso da 1ª pessoa: "))
maior = peso
menor = peso
for c in range(2, 6):
    peso = float(input("Digite o peso da {}ª pessoa: ".format(c)))
    if peso > maior:
        maior = peso
    elif peso < menor:
        menor = peso
print("Os menor peso lido foi de {:.1f}Kg e o maior foi de {:.1f}Kg".format(menor, maior))


'''
Faça um programa que leia o peso de cinco pessoas.
No final, mostre qual foi o maior e o menor peso lidos.
'''
