from utilidades import dado

p = float(input("Digite o preço: R$ "))
print(f"A metade de {dado.moeda(p)} é {dado.metade(p, True)}")
print(f"O dobro de {dado.moeda(p)} é {dado.dobro(p, True)}")
print(f"Aumentando 10%, temos {dado.aumentar(p, 10, True)}")
print(f"Reduzindo 13%, temos {dado.diminuir(p, 13, True)}")


'''
Modifique as funções que foram criadas no desafio 107
para que elas aceitem um parâmetro a mais, informando
se o valor retornado por elas vai ser ou não formatado
pela função moeda(), desenvolvida no desafio 108.
'''