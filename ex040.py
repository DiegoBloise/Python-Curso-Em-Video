n1 = float(input('Informe a primeira nota: '))
n2 = float(input('Informe a segunda nota: '))
m = (n1 + n2) / 2
if m < 5:
    print('''Média: {:.1f}
\033[1;31mREPROVADO\033[m'''.format(m))
elif m >= 5 and m < 7:
    print('''Média: {:.1f}
\033[1;33mRECUPERAÇÃO\033[m'''.format(m))
else:
    print('''Média: {:.1f}
\033[1;32mAPROVADO\033[m'''.format(m))

'''
Pode usar também: if 7 > m >= 5:
                  etc.
'''

'''
Crie um programa que leia duas notas de um aluno
e calcule sua média, mostrando uma mensagem no final,
de acordo com a média atingida:
-Média abaixo de 5.0:
REPROVADO
-Média entre 5.0 e 6.9:
RECUPERAÇÃO
-Média 7.0 ou superior:
APROVADO
'''
