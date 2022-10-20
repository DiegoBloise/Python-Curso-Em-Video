from time import sleep

cores = {
    'verde': '\033[0;30;42m',
    'azul': '\033[0;30;44m',
    'vermelho': '\033[0;30;41m',
    'branco': '\033[7;30m',
    'limpa': '\033[m'
    }

def titulo(msg, cor):
    tam = len(msg) + 4
    print(cores[cor])
    print('~' * tam)
    print(f'  {msg}  ')
    print('~' * tam)
    print(cores['limpa'])


while True:
    titulo('SISTEMA DE AJUDA PyHELP', 'verde')
    func = str(input('Função da Biblioteca > '))
    if func.lower() == 'fim':
        break
    else:
        titulo(f"Acessando o manual do comando '{func}'", 'azul')
        sleep(2)
        cores['branco']
        help(func)
        cores['limpa']
titulo('ATÉ LOGO!', 'vermelho')
sleep(2)


'''
Faça um mini-sistema que utilize o Interactive Help do Python.
O usuário vai digitar o comando e o manual vai aparecer.
Quando o usuário digitar a palavra 'FIM', o programa se encerrará.
OBS: use cores.
'''