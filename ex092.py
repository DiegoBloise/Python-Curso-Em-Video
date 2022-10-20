from datetime import date

anoAtual = date.today().year

pessoa = {}

pessoa['Nome'] = str(input('Nome: '))
anoNascimento = int(input('Ano de nascimento: '))
pessoa['Idade'] = anoAtual - anoNascimento
ctps = int(input('Carteira de trabalho (0 não tem): '))
if ctps > 0:
    pessoa['CTPS'] = ctps
    pessoa['Contratação'] = int(input('Ano de contratação: '))
    pessoa['Salário'] = float(input('Salário: R$ '))
    pessoa['Aposentadoria'] = (pessoa['Contratação'] + 35) - anoNascimento

print('\n', pessoa)
print()
for k,v in pessoa.items():
    print(f'{k} tem o valor {v}')
if ctps == 0:
    print(f"{pessoa['Nome']} não tem carteira de trabalho.")


'''
Crie um programa que leia nome, ano de nascimento e carteira de trabalho e
cadastre-os (com idade) em um dicionário se por acaso a CTPS for diferente
de ZERO, o dicionário receberá também o ano de contratação e o salário.
Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
'''