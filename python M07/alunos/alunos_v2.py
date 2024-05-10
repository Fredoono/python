"""
Programa para guardar dados de vários alunos em um ficheiro de texto
Neste projeto os dados estão todos só no ficheiro e são lidos/escritos quando é necessário
"""
import utils, os


#nome do ficheiro
nome_ficheiro = "alunos2.txt"

def criar_aluno():
    """Função para ler os seguintes dados:
    Nome, morada, email e idade de um aluno
    Devolve um dicionário com os dados"""
    nome = utils.le_texto("insira o nome do aluno a adicionar: ")
    morada = utils.le_texto("insira a morada: ")
    email = utils.le_email("insira o email do aluno: ")
    idade = utils.le_numero("insira a idade do aluno:")
    aluno = {
        "nome":nome,
        "morada":morada,
        "email":email,
        "idade":idade, }  
    return aluno

def listar():
    """Função para listar os alunos do ficheiro"""
    if verificar():
        return
    with(open(nome_ficheiro,"r",encoding="utf-8")) as ficheiro:
        while True:
            linha = ficheiro.readline()
            if not linha:
                break
            aluno = linha.split(",")
            print (aluno)

def verificar():
    return os.path.exists(nome_ficheiro) == False

def adicionar():
    """Função para adicionar um aluno ao ficheiro"""
    aluno = criar_aluno()
    with(open(nome_ficheiro,"a",encoding="utf-8")) as ficheiro:
        ficheiro.write(f"{aluno['nome']}, {aluno['morada']}, {aluno['email']}, {aluno['idade']} \n")

def apagar():
    """função para apagar um aluno do ficheiro"""
    if verificar():
        return
    nome = utils.le_texto("insira o nome de quem quer apagar")
    with(open(nome_ficheiro,"r",encoding="utf-8")) as ficheiro:
        with(open("temp.txt","w",encoding="utf-8")) as f_escrita:
            while True:
                linha = ficheiro.readline()
                if not linha:
                    break
                aluno = linha.split(",")
                if aluno[0] != nome:
                    f_escrita.write(linha)
    #apagar o ficheiro
    os.remove(nome_ficheiro)
    os.rename("temp.txt",nome_ficheiro)
 
def pesquisar():
    """função para pesquisar uma pessoa"""
    if verificar():
        return
    nome = utils.le_texto("insira o nome de quem quer pesuisar: ")
    with(open(nome_ficheiro,"r",encoding="utf-8")) as ficheiro:
        while True:
            linha = ficheiro.readline()
            if not linha:
                break
            aluno = linha.split(",")
            if nome.lower() in aluno[0].lower():
                print (aluno[0])
def main():
    while True:
        op=utils.menu("Ficheiros Texto",["Adicionar","Listar","Apagar","Pesquisar","Terminar"])
        if op==1:
            adicionar()
        if op==2:
            listar()
        if op==3:
            apagar()
        if op ==4:
            pesquisar()
        if op == 4:
            break

if __name__=="__main__":
    main()