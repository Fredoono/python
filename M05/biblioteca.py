import numpy as np
#21/02/2024
# Função que permite ao utilizador adicionar um livro
# O livro novo estará sempre disponivel
# Verifique se ainda existe espaço no array antes de adicionar
# Tenha atenção para não repetir o id do livro
def adicionar_livro(livros,nr_livros):
    if nr_livros != 100:
        titulo = input("insira o título do livro que quer inserir: ")
        id = livros[nr_livros-1]["id_livro"]+1
        livros[nr_livros] = {"id_livro":id,"titulo": titulo, "disponivel": True,"nome_leitor":""}
        print ("o livros está adicionado.")
        return(nr_livros)
    else:
        print ("nao á espaço para mais livros")

# Função para mostrar os livros
# deve permitir escolher se lista todos ou só os disponíveis ou só os indisponíveis
def listar_livros(livros, nr_livros):
    op = input("1- listar tudo 2- listar disponiveis 3- listar indisponiveis")
    if op == "1":
        for i in range (nr_livros):
            for chave,valor in livros[i].items():
                print(f"{chave}-{valor}")
            print ("#"*20)
    if op == "2" or op == "3":
        escolha = True if op == "2" else False
        for i in range (nr_livros):
            if livros[i]["disponivel"] == escolha:
                for chave,valor in livros[i].items():
                    print(f"{chave}-{valor}")
                print ("#*20")
# Função que muda o estado do livro e regista o nome do leitor
def emprestar_livro(livros, nr_livros):
    numero = int(input("qual o id do livro que quer inserir: "))
    for i in range (nr_livros):
        if livros[i]["id_livro"] == numero and livros[i]["disponivel"] == True:
            nome = input("insira o nome da pessoa que vai levar o livro: ")
            livros[i]["disponivel"] = False
            livros[i]["nome_leitor"] = nome  
            return
    print ("nao está disponivel nenhum livro com esse id")
    
    print("este livro nao existe ou nao está disponivel")

#Função que torna o livro disponível e apaga o nome do leitor
def devolver_livro(livros, nr_livros):
    numero = int(input("qual o id do livro que quer inserir: "))
    for i in range (nr_livros):
        if livros[i]["id_livro"] == numero and livros[i]["disponivel"] == False:
            livros[i]["disponivel"] = True
            livros[i]["nome_leitor"] = ""
        else:
            print("este livro nao existe ou está disponivel")
#função que elemina um livro permanentemente
def eleminar_livros(livros, nr_livros):
    id = input("qual o id do livros que quer eliminar? ")
    for i in range (nr_livros):
        if livros[i]["id_livro"] == id:
            for l in range (nr_livros-1,i,-1):
                livros[l] = livros[l+1]
            nr_livros -= 1
            return(nr_livros)
    print ("não existe o livro indicado")
#função que procura todos os livros do utilizador X
def procurar_livros(livros, nr_livros):
    nome = input("insira o nome do leitor que quer procurar")
    for i in range(nr_livros):
        if livros[i]["nome_leitor"] == nome:
            print (livros[i]["titulo"])

#Função que apresenta as opções ao utilizador e devolve a sua escolha
def menu(livros, nr_livros):
    while True:
        op = input(f"1- adicionar livros\n 2- listar livros\n 3- emprestar um livro\n 4- devolver um livro\n 5-eliminar um livro\n 6- procurar todos os livros de um leitor\n 7- sair")
        if op == "1":
            adicionar_livro(livros,nr_livros)
            nr_livros = adicionar_livro(livros,nr_livros)
        elif op == "2":
            listar_livros(livros, nr_livros)
        elif op == "3":
            emprestar_livro(livros, nr_livros)
        elif op == "4":
            devolver_livro(livros, nr_livros)
        elif op == "5":
            eleminar_livros(livros, nr_livros)
            nr_livros = adicionar_livro(livros,nr_livros)  
        elif op == "6":
            procurar_livros(livros, nr_livros)
        elif op == "7":
            break
        else: 
            pass
#função para gerar (seed) dados iniciais
def inicializar(livros):
    livros[0]={"id_livro":1,"titulo": "Dom Quixote", "disponivel": True,"nome_leitor":""}
    livros[1]={"id_livro":2,"titulo": "A Arte da Guerra", "disponivel": True,"nome_leitor":""}
    livros[2]={"id_livro":3,"titulo": "1984", "disponivel": True,"nome_leitor":""}
    livros[3]={"id_livro":4,"titulo": "Os Lusíadas", "disponivel": True,"nome_leitor":""}
    livros[4]={"id_livro":5,"titulo": "A Metamorfose", "disponivel": True,"nome_leitor":""}
    return 5

def main():
    MAX_ITEMS=100
    livros =np.empty(MAX_ITEMS,dtype=object)
    nr_livros=inicializar(livros)
    id = 6
    menu(livros, nr_livros)
    nr_livros = menu
# Ponto de entrada do programa (main loop)
if __name__ == "__main__":
    main()
