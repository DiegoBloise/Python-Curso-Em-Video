def moeda(p):
    formatado = f"R${p:.2f}".replace('.', ',')
    return formatado


def aumentar(p, percent, formatado=False):
    novoPreco = p + (p * percent / 100)
    return moeda(novoPreco) if formatado else novoPreco


def diminuir(p, percent, formatado=False):
    novoPreco = p - (p * percent / 100)
    return moeda(novoPreco) if formatado else novoPreco


def dobro(p, formatado=False):
    dobro = p * 2
    return moeda(dobro) if formatado else dobro


def metade(p, formatado=False):
    metade = p / 2
    return moeda(metade) if formatado else metade


def resumo(p, aument, reduc):
    print('-'*31)
    print(f"{'RESUMO DO VALOR':^31}")
    print('-'*31)
    print(f"Preço analisado.....:{moeda(p)}")
    print(f"Dobro do preço......:{dobro(p, True)}")
    print(f"Metade do preço.....:{metade(p, True)}")
    print(f"{aument}% de aumento......:{aumentar(p, aument, True)}")
    print(f"{reduc}% de redução......:{diminuir(p, reduc, True)}")
    print('-'*31)
