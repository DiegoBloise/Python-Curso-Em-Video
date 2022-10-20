exp = str(input('Digite a expressão: '))

if exp.index(')') < exp.index('(') or exp[::-1].index('(') < exp[::-1].index(')') or exp.count('(') != exp.count(')'):
    print('\033[31mExpressão Incorreta!\033[m')
else:
    print('\033[32mExpressão Correta!\033[m')

#########################################################################

exp = str(input('Digite a expressão: '))
pilha = []
for simb in exp:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('\033[32mExpressão Correta!\033[m')
else:
    print('\033[31mExpressão Incorreta!\033[m')


'''
Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
Seu aplicativo deverá analisar se a expressão passada está com os parênteses
abertos e fechados na ordem correta.
'''