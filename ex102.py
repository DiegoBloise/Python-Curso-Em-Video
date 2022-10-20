def fatorial(n, show=False):
    """
    -> Calcula o fatorial de um número.
    :param n: O número a ser calculado.
    :param show: (opcional) Mostrar ou não a conta.
    :return: O valor do fatorial de um número n.
    """
    tot = 1
    for num in range(n, 0, -1):
        tot *= num
        if show:
            if num > 1:
                print(f'{num} X ', end='')                                
            else:
                print(f'{num} = ', end='')
    return tot


print(fatorial(5, True))
#help(fatorial)


'''
Crie um programa que tenha uma função fatorial() que receba dois parâmetros:
o primeiro que indique o número a calcular e o outro chamado show,
que será um valor lógico (opcional) indicando se será mostrado
ou não na tela o processo de cálculo do fatorial.
'''