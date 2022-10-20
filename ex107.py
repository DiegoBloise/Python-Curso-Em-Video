from utilidades import dado

p = float(input("Digite o preço: R$ "))
print(f"A metade de R${p} é R$ {dado.metade(p):.2f}")
print(f"O dobro de R${p} é R$ {dado.dobro(p):.2f}")
print(f"Aumentando 10%, temos R$ {dado.aumentar(p, 10):.2f}")
print(f"Reduzindo 13%, temos R$ {dado.diminuir(p, 13):.2f}")


'''
Crie um módulo chamado moeda.py que tenha as funções incorporadas
aumentar(), diminuir(), dobra(), e metade().
Faça também um programa que importe esse módulo e use
algumas dessas funções.
'''