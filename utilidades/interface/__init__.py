from os import system

def top(prompt):
    system("cls")
    print("-="*25)
    print(f"{prompt:^50}")
    print("-="*25)
    print("")

def opcoes(lista):
    for i in range(len(lista)):
        print(f"[{i+1}] {lista[i]}")
