from time import sleep

def contador(i, f, p):
    if p == 0:
        p = 1
    elif p < 0:
        p *= -1
    print('-=' * 30)
    print(f'Contando de {i} até {f}, de {p} em {p}...')
    sleep(1)
    if i < f:
        for n in range(i, f+p, p):
            sleep(0.7)
            if n > f:
                break
            print(f'{n}...', end='', flush='True')
    elif i > f:
        for n in range(i, f-p, -p):       
            sleep(0.7)
            if n < f:
                break
            print(f'{n}...', end='', flush='True')
    print('FIM!')


contador(1, 10, 1)
contador(10, 0, 2)
print('-=' * 30)
print('Contagem Personalizada:')
contador(int(input(f'{"Início: ":8}')), int(input(f'{"Fim: ":8}')), int(input(f'{"Passo: ":8}')))


'''
Faça um programa que tenha uma função chamada contador(), que
receba três parâmetros: início, fim e passo e realize a contagem.

Seu programa tem que realizar três
contagens através da função criada:

A)De 1 até 10, de 1 em 1
B)De 10 até 0, de 2 em 2
C)Uma contagem personalizada
'''