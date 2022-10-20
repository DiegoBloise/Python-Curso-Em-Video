valores = list()
for c in range(1, 6):
    valor = int(input(f'Digite o {c}º valor: '))
    if c == 1 or valor > valores[-1]:
        valores.append(valor)
    else:
        for p, v in enumerate(valores):
            if valor <= v:
                valores.insert(p, valor)
                break
print(valores)


'''
Crie um programa onde o usuário possa digitar cinco valores numéricos e
cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()).
No final, mostre a lista ordenada na tela.
'''
