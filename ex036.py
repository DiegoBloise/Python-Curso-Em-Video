import os
pcount = 1
while pcount == 1:
    count = 1
    os.system('clear')
    escolha = int(input('''Escolha O Programa:
[1]   [2]  >>> '''))
    if escolha == 1:
        os.system('clear')
        print('-=' * 40)
        while count == 1:
            os.system('clear')
            valimo = float(input('Qual o valor do imóvel? >>> R$'))
            sal = float(input('Qual o valor do seu salário? >>> R$'))
            anos = int(input('Quer pagar em quantos anos? >>> '))
            meses = anos * 12
            prest = valimo / meses
            rndisp = (sal * 30) / 100
            if rndisp >= prest:
                os.system('clear')
                print('-=' * 40)
                print('''Empréstimo \033[1;32mAPROVADO\033[m!
Você irá pagar o valor de R${:.2f} por mês
Durante {} anos'''.format(prest, anos))
                print('-=' * 40)
            else:
                os.system('clear')
                print('-=' * 40)
                print('''Empréstimo \033[31mNEGADO\033[m!
Infelizmente você é pobre demais para adquirir este imóvel!
Aumente o número de anos ou procure um emprego melhor!
Renda mínima disponível para aquisição do imóvel: R${:.2f}'''.format(prest))
                print(
                    'Renda disponível para aquisição do imóvel: R${:.2f}  (30% do salário) '.format(rndisp))
                print('-=' * 40)
            count = int(input('''Executar Novamente?
[1]SIM    [2]NÃO >>> '''))
    elif escolha == 2:
        os.system('clear')
        print('-=' * 40)
        while count == 1:
            os.system('clear')
            valimo = float(input('Qual o valor do imóvel? >>> R$'))
            sal = float(input('Qual o valor do seu salário? >>> R$'))
            rndisp = (sal * 30) / 100
            meses = valimo / rndisp
            anos = meses / 12
            os.system('clear')
            print('-=' * 40)
            print('''Você irá quitar o imóvel em {:.0f} meses ({:.0f} anos)
Pagando o valor de R${:.2f} por mês.'''.format(meses, anos, rndisp))
            print('-=' * 40)
            count = int(input('''Executar Novamente?
[1]SIM    [2]NÃO >>> '''))
    os.system('clear')
    pcount = int(input('''\nSelecionar outro programa?
[1]SIM    [2]NÃO >>> '''))
os.system('clear')

print('-=' * 40)
print('\nPROGRAMA ENCERRADO...\n')
print('-=' * 40)
print('\n' * 15)


'''
Escreva um programa para aprovar o empréstimo bancário
para a compra de uma casa.
O programa vai perguntar o valor da casa, o salário do
comprador e em quantos anos ele vai pagar.
Calcule o valor da prest mensal, sabendo que ela
não pode exceder 30% do salário ou então
o empréstimo será negado.
'''
