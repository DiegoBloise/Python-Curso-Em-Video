n = int(input('Digite um valor: '))
maior = menor = soma = n
cont = 0
c = 1
while cont != 'n':
    n = int(input('Digite outro valor: '))
    soma += n
    if n > maior:
        maior = n
    if n < menor:
        menor = n
    c += 1
    cont = input('Quer continuar?  [S/n]: ')
media = soma / c
print('-='*30)
print('''A média entre todos os {} valores digitados é igual {:.2f}
O menor valor digitado foi {} e o maior valor foi {}'''.format(c, media, menor, maior))
print('-='*30)


'''
Crie um programa que leia vários números inteiros pelo teclado.
No final da execução, mostre a média entre todos os valores e
qual foi o maior e o menor valores lidos. O programa deve
perguntar ao usuário se ele quer ou não continuar a digitar valores.
'''
