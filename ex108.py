from utilidades import dado

p = float(input("Digite o preço: R$ "))
print(f"A metade de {dado.moeda(p)} é {dado.moeda(dado.metade(p))}")
print(f"O dobro de {dado.moeda(p)} é {dado.moeda(dado.dobro(p))}")
print(f"Aumentando 10%, temos {dado.moeda(dado.aumentar(p, 10))}")
print(f"Reduzindo 13%, temos {dado.moeda(dado.diminuir(p, 13))}")


'''
Adapte o código do desafio 107, criando uma função adicional
chamada moeda() que consiga mostrar os valores como um valor
monetário formatado.
'''