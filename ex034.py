sal = float(input('Qual o salário do funcionário? R$'))
if sal > 1250:
    novo = sal + ((sal * 10) / 100)
else:
    novo = sal + ((sal * 15) / 100)
print('O novo salário será de R${:.2f}'.format(novo))


'''
Escreva um programa que pergunte o salário de um funcionário calcule o valor do seu aumento.
Para salários superiores a R$1250,00, calcule um aumento de 10%.
Para os inferiores ou iguais, o aumento é de 15%.
'''
