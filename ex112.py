from utilidades import moeda, dado

p = moeda.leiaDinheiro("Digite o preço: R$")
dado.resumo(p, 35, 22)


'''
Dentro do pacote utilidades que criamos no desafio 111,
temos um módulo chamado dado. Crie uma função chamada
leiaDinheiro() que seja capaz de funcionar como a função
input(), mas com uma validação de dados para aceitar
apenas valores que sejam monetários.
'''
