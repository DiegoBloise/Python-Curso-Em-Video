nums = (int(input('Primeiro valor: ')), int(input('Segundo valor: ')),
        int(input('Terceiro valor: ')), int(input('Quarto valor: ')))
print(f'Os valores digitados foram {nums}')
if 9 in nums:
    print(f'O valor 9 apareceu {nums.count(9)} vezes.')
else:
    print('O valor 9 não foi digitado!')
if 3 in nums:
    print(f'O valor 3 foi digitado na {(nums.index(3))+1}ª posição.')
else:
    print('O valor 3 não foi digitado!')
p = 0
for v in nums:
    if v % 2 == 0:
        p += 1
        if p == 1:
            print('Os valores pares digitados foram: ', end='')
        print(v)            
    else:
        print('Não foram digitados valores pares!')


'''
Desenvolva um programa que leia quatro valores pelo teclado
e guarde os em uma tupla. No final, mostre:
A) Quantas vezes apareceu o valor 9.
B) Em que posição foi digitado o primeiro valor 3.
C) Quais foram os números pares.
'''
