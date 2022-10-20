while True:
    n = int(input('Quer ver a tabuada de qual valor: '))
    print('-='*18)
    if n < 1:
        break
    for c in range(1, 11):
        print(f'{n} x {c} = {n*c}')
    print('-='*18)
print('Programa Encerrado.')


'''
Faça um programa que mostre a tabuada de vários números, um de cada vez,
para cada valor digitado pelo usuário. O programa será interrompido
quando o número solicitado for negativo.
'''
