frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
frase = ''.join(palavras)
contrario = frase[::-1]
print('O contrário de {} é {}'.format(frase, contrario))
if frase == contrario:
    print('Então, a frase é um palíndromo!')
else:
    print('Então, a frase não é um palíndromo!')


'''
Crie um programa que leia uma frase qualquer e diga
se ela é um palíndromo, desconsiderando os espaços.
Ex:
   APOS A SOPA
   A SACADA DA CASA
   A TORRE DA DERROTA
   O LOBO AMA O BOLO
   ANOTARAM A DATA DA MARATONA
'''
