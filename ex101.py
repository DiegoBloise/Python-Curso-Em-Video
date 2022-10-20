from datetime import date

def voto(idade):
    if idade < 18:
        return f'Com {idade} anos: NÃO VOTA.'
    elif 18 <= idade < 65:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO.'
    else:
        return f'Com {idade} anos: VOTO OPCIONAL.'


anoAtual = date.today().year

idade = anoAtual - int(input('Em que ano você nasceu?: '))
print(voto(idade))


'''
Crie um programa que tenha uma função chamada voto() que
vai receber como parâmetro o ano de nascimento de uma pessoa,
retornando um valor literal indicando se uma pessoa tem voto
NEGADO, OPCIONAL ou OBRIGATÓRIO nas eleições.
'''