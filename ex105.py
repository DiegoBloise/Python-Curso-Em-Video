def notas(*n, sit=False):
    """
    -> Função para analisar notas e situações de vários alunos.
    :param n: uma ou mais notas dos alunos (aceita várias).
    :param sit: valor opcinal, indicando se deve ou não adicionar a situação.
    :return: dicionário com várias informações sobre a situação da turma.
    """
    dicionarioNotas = {
        'Total': float(f"{len(n):.1f}"),
        'Maior': float(f"{max(n):.1f}"),
        'Menor': float(f"{min(n):.1f}"),
        'Média': float(f"{sum(n) / len(n):.1f}"),
    }
    if sit:
        if dicionarioNotas['Média'] >= 8:
            dicionarioNotas['Situação'] = 'BOA'
        elif dicionarioNotas['Média'] >= 5:
            dicionarioNotas['Situação'] = 'RAZOÁVEL'
        else:
            dicionarioNotas['Situação'] = 'RUIM'
    return dicionarioNotas
    
resp = notas(9, 9, 9, 9, sit=True)
print(resp)
#help(notas)


'''
Faça um programa que tenha uma função notas() que pode receber várias
notas de alunos e vai retornar um dicionário com as seguintes informações:

- Quantidade de notas
- A maior nota
- A menor nota
- A média da turma
- A situação (opcional)

Adicione também as docstrings da função.
'''