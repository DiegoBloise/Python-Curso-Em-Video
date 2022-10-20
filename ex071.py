saque = int(input('Qual valor do saque? R$'))
ced = 100
totalced = 0
while True:
    if saque >= ced:
        saque -= ced
        totalced += 1
    else:
        if totalced > 0:
            print(f'Total de {totalced} cédulas de R${ced}')
        if ced == 100:
            ced = 50
        elif ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 5
        elif ced == 5:
            ced = 1

        totalced = 0

        if saque == 0:
            break


'''
Crie um programa que simule o funcionamento de um caixa eletrônico.
No início, pergunte ao usuário qual será o valor a ser sacado
(número inteiro) e o programa vai informar quantas cédulas
de cada valor serão entregues.
OBS: Considere que o caixa possui cédulas de
R$50, R$20, R$10, R$1.
'''
