homens = maiores = mulheres = 0
while True:
    idade = int(input('Informe a idade: '))
    sexo = str(input('Informe o sexo [M/F]: ')).upper()
    cont = input('Quer continuar? [S/n]: ')
    if sexo == 'M':
        homens += 1
    if idade >= 18:
        maiores += 1
    if sexo == 'F' and idade < 20:
        mulheres += 1
    if cont == 'n':
        break
print(f'''Pessoas com mais de 18 anos: {maiores}
Total de homens cadastrados: {homens}
Total de mulheres com menos de 20 anos: {mulheres}''')


'''
Crie um programa que leia a idade e o sexo de várias pessoas.
A cada pessoa cadastrada, o programa deverá perguntar se o usuário
quer ou não continuar. No final, mostre:
A) Quantas pessoas tem mais de 18 anos.
B) Quantos homens foram cadastrados.
C) Quantas mulheres tem menos de 20 anos.
'''
