caros = 0
barato = produto = str(input('Nome do produto: '))
tot = pbarato = preço = float(input('Preço do produto: R$'))
while True:
    if preço > 1000:
        caros += 1
    cont = input('Quer continuar? [S/n]: ')
    if cont == 'n':
        break
    produto = str(input('Nome do produto: '))
    preço = float(input('Preço do produto: R$'))
    if preço < pbarato:
        barato = produto
    tot += preço
print(f'''Total gasto na compra: R${tot:.2f}
Total de produtos acima de R$1000: {caros}
Produto mais barato: {barato}''')

'''
Crie um programa que leia o nome e o preço de vários produtos.
O programa deverá perguntar se o usuário vai continuar,
No final, mostre:
A) Qual é o total gasto na compra.
B) Quantos produtos custam mais de R$1000.
C) Qual é o nome do produto mais barato.
'''
