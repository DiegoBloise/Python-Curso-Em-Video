# from os import system
from time import sleep
from utilidades import interface

try:
    while True:
        interface.top("MENU PRINCIPAL")
        interface.opcoes(["Cadastrar nova pessoa", "Listar pessoas cadastradas", "Finalizar"])
        try:
            menu = int(input("\n\nOPÇÃO: "))
            if menu == 1:
                interface.top("CADASTRAR NOVA PESSOA")
                arquivo = open("ex115.txt", "a")
                nome = input("Nome: ")
                idade = input("Idade: ")
                linha = f"{nome:<43}{idade} Anos\n"
                arquivo.write(linha)
            elif menu == 2:
                interface.top("PESSOAS CADASTRADAS")
                try:
                    arquivo = open("ex115.txt")
                except FileNotFoundError:
                    print(f"Não há pessoas cadastradas...\n")
                else:
                    print(arquivo.read())
                print("-="*25)
                continuar = input("\nPressione enter para continuar...")
            elif menu == 3:
                interface.top("FINALIZANDO...")
                sleep(2)
                break
            else:
                raise ValueError
        except (ValueError, TypeError):
            print("\033[31;01mOpção Inválida! Tente novamente...\033[m")
            sleep(2)
finally:
    arquivo.close()


"""
Crie um pequeno sistema modularizado que permita cadastrar
pessoas pelo seu nome e idade em um arquivo de texto simples.

O sistema só vai ter 2 opções: cadastrar uma nova pessoa e
listar todas as pessoas cadastradas.
"""
