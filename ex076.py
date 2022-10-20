lista = ('Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90, 'Estojo', 25.00, 'Transferidor', 4.20,
         'Compasso', 9.99, 'Mochila', 120.32, 'Canetas', 22.30, 'Livro', 34.90)

print('-'*40)
print(f"{'LISTAGEM DE PREÇOS':^40}")
print('-'*40)
for p in lista:
    if type(p) == str:
        print(f'{p:.<30}R$ ', end='')
    else:
        print(f'{p:>6.2f}')
print('-'*40)


'''
Crie um programa que tenha uma tupla única com nomes
de produtos e seus respectivos preços, na sequência.
No final, mostre uma listagem de preços, organizando
os dados em forma tabular.
'''
