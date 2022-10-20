def leiaDinheiro(prompt):
    while True:
        valor = input(prompt)
        if (',' in valor and
                valor.count(',') == 1 and
                valor.replace(',', '').isnumeric()):
            return float(valor.replace(',', '.'))
        elif ('.' in valor and
                valor.count('.') == 1 and
                valor.replace('.', '').isnumeric() or
                valor.isnumeric()):
            return float(valor)
        else:
            print(f"ERRO: \"{valor}\" NÃO é um preço válido!")
