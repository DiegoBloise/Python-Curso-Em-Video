menu = 4
n1 = n2 = 0
print('{:=^20}'.format(' Calculadora '))
while menu != 0:
    if menu > 4:
        print('-'*25)
        print('''OPÇÃO INVÁLIDA!
TENTE NOVAMENTE.''')
    elif menu == 1:
        print('-='*20)
        print('\033[32mTotal da soma: {}\033[m'.format(n1 + n2))
        print('-='*20)
    elif menu == 2:
        print('-='*20)
        print('\033[32mTotal da multiplicação: {}\033[m'.format(n1 * n2))
        print('-='*20)
    elif menu == 3:
        if n1 > n2:
            print('-='*20)
            print('\033[32mO primeiro valor é o maior ({}).\033[m'.format(n1))
            print('-='*20)
        elif n2 > n1:
            print('-='*20)
            print('\033[32mO segundo valor é o maior ({}).\033[m'.format(n2))
            print('-='*20)
        else:
            print('-='*20)
            print('\033[32mOs dois valores são iguais.\033[m')
            print('-='*20)
    elif menu == 4:
        n1 = int(input('Digite o 1º valor: '))
        n2 = int(input('Digite o 2º valor: '))
    menu = int(input('''-------------------------
Selecione uma operação:
-------------------------
[1]SOMAR
[2]MULTIPLICAR
[3]MAIOR NÚMERO
[4]NOVOS NÚMEROS
[0]ENCERRAR

OPÇÃO:'''))
    print()

print('\033[32mPrograma Encerrado ;)\033[m')


'''
Crie um programa que leia dois valores
e mostre um menu na tela:

[1]somar
[2]multiplicar
[3]maior
[4]novos números
[5]sair do programa

Seu programa deverá realizar a operação solicitada em cada caso.
'''
