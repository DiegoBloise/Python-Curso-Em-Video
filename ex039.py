from datetime import date
ano = date.today().year
idade = ano - int(input('Informe o ano de nascimento: '))
if idade < 18:
    print('Você tem {} anos de idade e ainda faltam {} anos para se alistar ao serviço militar.'.format(
        idade, (18 - idade)))
elif idade == 18:
    print('Você tem {} anos de idade e já esta na hora de se alistar ao serviço militar.'.format(idade))
else:
    print('Você tem {} anos de idade e já se passou {} anos do prazo para se alistar ao serviço militar.'.format(
        idade, (idade - 18)))


'''
Faça um programa que leia o ano de nascimento de um jovem
e informe, de acordo com a sua idade:
-Se ele ainda vai se alistar ao serviço militar.
-Se é a hora de se alistar.
-Se ja passou do tempo de alistamento.
Seu programa também deverá mostrar o tempo
que falta ou que passou do prazo.
'''
