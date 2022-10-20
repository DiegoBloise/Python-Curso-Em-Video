def leiaInt(prompt):
    while True:
        try:
            n = int(input(prompt))
        except (ValueError, TypeError):
            print("ERRO: por favor, digite um número inteiro válido.")
        except KeyboardInterrupt:
            print("\nO usuário preferiu não digitar esse número.")
            return 0
        else:
            return n


def leiaFloat(prompt):
    while True:
        try:
            n = float(input(prompt))
        except (ValueError, TypeError):
            print("ERRO: por favor, digite um número real válido.")
        except KeyboardInterrupt:
            print("\nO usuário preferiu não digitar esse número")
            return 0
        else:
            return n
