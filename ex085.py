valores = [[], []]

for c in range(1, 8):
    entrada = int(input(f'Digite o {c}º valor: '))
    if entrada % 2 == 0:
        valores[0].append(entrada)
    else:
        valores[1].append(entrada)

print(f'Valores pares digitados: {sorted(valores[0])}')
print(f'Valores ímpares digitados: {sorted(valores[1])}')


'''
Crie um programa onde o usuário possa digitar sete valores numéricos
e cadastre-os em uma lista única que mantenha separados os valores
pares e ímpares. No final, mostre os valores pares e ímpares
em ordem crescente.
'''