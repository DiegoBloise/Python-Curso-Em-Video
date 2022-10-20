tot = 0
c = 0
n = int(input('Digite um número: '))
while n != 999:
    tot += n
    c += 1
    n = int(input('Digite outro número (999 para parar):  '))
print('A soma entre todos os {} números digitados é igual a {}'.format(c, tot))


'''
Crie um programa que leia vários números inteiros pelo teclado.
O programa só vai parar quando o usuário digitar o valor 999,
que é a condição de parada. No final, mostre quantos números
foram digitados e qual foi a soma entre eles (desconsiderando o flag).
'''
