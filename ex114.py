import urllib.request

try:
    urllib.request.urlopen("http://www.pudim.com.br/")
except Exception:
    print(f"\n\033[31;01mNão foi possível acessar o site!\033[m\n")
else:
    print("\n\033[32;01mSite acessado com sucesso!\033[m\n")


"""
Crie um código em python que teste se o site Pudim
está acessível pelo computador usado.
"""
