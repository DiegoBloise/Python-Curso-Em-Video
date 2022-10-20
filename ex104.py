def leiaInt(prompt):
    while True:
        num = input(prompt)
        if num.isnumeric():
            break
        else:
            print('ERRO: Valor Inválido!')
    return num


n = leiaInt('Digite um número: ')
print(f'O número digitado foi: {n}')


'''
Crie um programa que tenha a função leiaInt(), que vai funcionar
de forma semelhante à função input() do Python, só que fazendo
a validação para aceitar apenas um valor numérico.
EX:
    n = leiaInt('Digite um número:)
'''
