num = int(input('Digite um número inteiro: '))
option = int(input('''Escolha a qual será a base de conversão:
[1] BINÁRIO
[2] OCTAL
[3] HEXADECIMAL
OPÇÃO: '''))
if option == 1:
    print('{} convertido para BINÁRIO é igual a {}'.format(num, bin(num)[2:]))
elif option == 2:
    print('{} convertido para OCTAL é igual a {}'.format(num, oct(num)[2:]))
elif option == 3:
    print('{} convertido para HEXADECIMAL é igual a {}'.format(num, hex(num)[2:]))
else:
    print('OPÇÃO INVÁLIDA!')


'''
Escreva um programa que leia um número inteiro qualquer
e peça para o usuário escolher qual será a base de conversão:
-1 para binário
-2 para octal
-3 para hexadecimal
'''
