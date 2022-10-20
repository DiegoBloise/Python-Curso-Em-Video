from datetime import date
ano = date.today().year
idade = ano - int(input('Informe o ano de nascimento: '))
if idade <= 9:
    print('{} anos:MIRIM'.format(idade))
elif idade >= 10 and idade <= 14:
    print('{} anos:INFANTIL'.format(idade))
elif idade >= 15 and idade <= 19:
    print('{} anos:JUNIOR'.format(idade))
elif idade == 20:
    print('{} anos:SÊNIOR'.format(idade))
else:
    print('{} anos:MASTER'.format(idade))


'''
Pode usar também: if idade <= 9:
                  elif idade <= 14:
                  etc.
'''

'''
A Confederação Nacional de Natação precisa de um
programa que leia o ano de nascimento de um atleta
e mostre sua categoria, de acordo com a idade:
-Até 9 anos:MIRIM
-Até 14 anos:INFANTIL
-Até 19 anos:JUNIOR
-Até 20 anos:SÊNIOR
-Acima:MASTER
'''
