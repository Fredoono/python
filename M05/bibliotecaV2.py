
# Função que permite ao utilizador adicionar um livro
# O livro novo estará sempre disponivel
# Tenha atenção para não repetir o id do livro
def adicionar_livro(lista): 
    titulo = input("insira o titulo do livro que quer adicionar: ")
    if len(lista)>0:
        Id = lista[len(lista)-1]["id_livro"]+1
    else:
        Id = 1
    novo = {"id_livro":Id,"titulo":titulo,"diponivel":True,"nome_leitor":""}
    lista.append(novo)

# Função para mostrar os livros
# deve permitir escolher se lista todos ou só os disponíveis ou só os indisponíveis
def listar_livros(livros):
    op = input("1- listar tudo 2- listar disponiveis 3- listar indisponiveis")
    for livro in livros:
        if op == "1" or (op == "2" and livro["disponivel"] == True) or (op == "3" and livro["disponivel"] == False):
            for chave,valor in livros.items():
                print(f"{chave}: {valor}")


# Função que muda o estado do livro e regista o nome do leitor
def emprestar_livro(livros):
    op = int(input("insira livro é para emprestar: "))
    for livro in livros:
        if op == livro["id_livro"]:
            if livro["disponivel"] == False:
                print ("o livro nao está disponivel")
                return
            nome = input("qual o nome do leitor? ")
            livro["disponivel"] = False
            livro["nome_leitor"] = nome
            print ("o livro foi entregue")
            return
    print ("nao existe tal livro")


#Função que torna o livro disponível e apaga o nome do leitor
def devolver_livro(livros):
    op = int(input("insira livro é para emprestar: "))
    for livro in livros:
        if op == livro["id_livro"]:
            if livro["disponivel"] == True:
                print ("o livro nao está indisponivel")
                return
            livro["disponivel"] = True
            livro["nome_leitor"] = ""
            print ("o livro foi devolvido")
            return
    print ("nao existe tal livro")

#Função que apresenta as opções ao utilizador e devolve a sua escolha
def menu(lista, pos):
    while True:
        print("1. Adicionar\n2.Listar\n3.Emprestar\n4.Devolver\n5.Sair")
        op = int(input(":"))
        if op <1 or op >5:
            print("Essa opção não é válida")
        if op == 1:
            adicionar_livro(lista)
        elif op == 2:
            listar_livros(lista)
        elif op == 3:
            emprestar_livro(lista)
        else:
            return op

#função para gerar (seed) dados iniciais
def inicializar(livros):
    livros.append({"id_livro":1,"titulo": "Dom Quixote", "disponivel": True,"nome_leitor":""})
    livros.append({"id_livro":2,"titulo": "A Arte da Guerra", "disponivel": True,"nome_leitor":""})
    livros.append({"id_livro":3,"titulo": "1984", "disponivel": True,"nome_leitor":""})
    livros.append({"id_livro":4,"titulo": "Os Lusíadas", "disponivel": True,"nome_leitor":""})
    livros.append({"id_livro":5,"titulo": "A Metamorfose", "disponivel": True,"nome_leitor":""})

def main():
    livro = []
    pos = inicializar(livro)
    menu(livro, pos)

# Ponto de entrada do programa (main loop)
if __name__ == "__main__":
    main()