sex = ''
while sex != 'M' and sex != 'F':
    sex = str(input('Informe seu sexo [M/F]:')).upper()
    if sex != 'M' and sex != 'F':
        print('Entrada Inválida! Tente Novamente.')
print('Sexo Selecionado:{}'.format(sex))


'''
Faça um programa que leia o sexo de uma pessoa,
mas só aceite os valores 'M' ou 'F'.
Caso esteja errado, peça a digitação novamente
até ter um valor correto.
'''
