from os import system
prc = float(input('Preço do produto: R$'))
system('clear')
print('Selecione a forma de pagamento:')
print('[1] - À vista dinheiro/cheque:10% de desconto')
print('[2] - À vista no cartão:5% de desconto')
print('[3] - Em até 2x no cartão:preço normal')
print('[4] - 3x ou mais no cartão:20% de juros')
fp = int(input("OPÇÃO: "))
system('clear')
if fp == 1:
    total = prc - (prc*10) / 100
elif fp == 2:
    total = prc - (prc*5) / 100
elif fp == 3:
    total = prc
else:
    total = prc + (prc * 20) / 100
print('-=-'*20)
print('TOTAL A PAGAR R${:.2f}'.format(total))
print('-=-'*20)


'''
Elabore um programa que calcule o valor a ser
pago por um produto, considerando o seu
preço normal e condição de pagamento:
-À vista dinheiro/cheque:10% de desconto
-À vista no cartão:5% de desconto
-Em até 2x no cartão:preço normal
-3x ou mais no cartão:20% de juros
'''
