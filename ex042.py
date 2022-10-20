r1 = float(input('Comprimento da primeira reta: '))
r2 = float(input('Comprimento da segunda reta: '))
r3 = float(input('Comprimento da terceira reta: '))
if (r1+r2) > r3 and (r1+r3) > r2 and (r2+r3) > r1:
    print('As três retas podem formar um triângulo!')
    if r1 == r2 and r1 == r3 and r2 == r3:
        print('Triângulo Equilátero: todos os lados iguais.')
    elif r1 != r2 and r1 != r3 and r2 != r3:
        print('Triângulo Escaleno: todos os lados diferentes')
    else:
        print('Triângulo Isósceles: dois lados iguais.')
else:
    print('As três retas NÃO podem formar um triângulo!')


'''
Pode usar também: if r1 == r2 == r3:
                  elif r1 != r2 != r3 != r1

'''
'''
Refaça o DESAFIO 035 dos triângulos, acrescentando o
recurso de mostrar que tipo de triângulo será formado:
-Equilátero:todos os lados iguais
-Isósceles:dois lados iguais
-Escaleno:todos os lados diferentes
'''
