#Frederico Sousa 24585
def le_numero(titulo):
    """função que lê e devolve um inteiro do utilizador"""
    temp=input(titulo)
    while not temp.isnumeric():
        temp=input(titulo)
    return int(temp)

def le_texto(titulo,minimo=None):
    """função para ler um texto com um número minimo de letras"""
    temp=input(titulo)
    while minimo is not None and len(temp)<minimo:
        temp=input(titulo)
    return temp

def mostrar_menu(titulo,opcoes):
    """função para mostrar um menu
    p.ex.: mostrar_menu("Menu Principal",["Livros","Leitores",...])"""
    print ("")
    print("="*40)
    print(titulo)
    print("="*40)
    for i in range(len(opcoes)):
        print(f"{i+1} - {opcoes[i]}")
    print("="*40)

def menu(titulo, opcoes):
    """Função para mostrar e ler uma opção válida de um menu"""
    mostrar_menu(titulo,opcoes)
    nr_opcoes=len(opcoes)
    while True:
        op=int(input("Opção:"))
        if op>=1 and op<=nr_opcoes:
            break
        print("Opção inválida")
    return op
