frase = str(input('Digite uma frase:')).strip().lower()
print('A letra "a" aparece {} vezes'.format(frase.count('a')))
print('''Primeiro na posição {}
e por último na posição {}'''.format(frase.find('a')+1, frase.rfind('a')+1))


'''
Faça um programa que leia uma frase pelo teclado e mostre:
Quantas vezes aparece a letra"A".
Em que posição ela aparece a primeira vez.
Em que posição ela aparece a última vez.
'''
