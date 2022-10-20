valores = []
valores.append(int(input('Digite um valor: ')))
while True:
    valor = int(input('Digite outro valor: '))
    if valor not in valores:
        valores.append(valor)
    resp = str(input('Continuar? [S]im / [N]ão : '))
    if resp in 'Nn':
        break
print(f'Valores únicos digitados: {sorted(valores)}')


'''
Crie um programa onde o usuário possa digitar vários valores numéricos
e cadastre-os em uma lista. Caso o número ja exista la dentro,
ele não será adicionado. No final, serão exibidos todos
os valores únicos digitados, em ordem crescente.
'''