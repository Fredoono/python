#programa para gerir alunos
#um array com 100 posições
#adicionar alunos 
#pesquisar alunos
#editar alunos
import numpy as np


def adicionar_aluno():
    nome = input ("insira o nome: ")
    idade = input ("insira a idade: ")
    morada = input ("insira a morada: ")
    email = input ("insira o email: ")
    novo = {"nome":nome, "idade":idade, "morada":morada, "email":email}
    return novo

def procurar_aluno(alunos,pos):
    nome = input("insira o nome do aluno: ")

    for i in range(pos):
        if alunos[i]["nome"] == nome:
            return alunos[i]
    return None

def procurar_posição(alunos,pos):
    nome = input("insira o nome do aluno: ")
    for i in range( pos):
        if alunos[i]["nome"] == nome:
            return i
    return None


def listar_alunos(alunos, pos):
    for i in range(pos):
        aluno = alunos[i]
        for key,val in aluno.items():
            print (f" {key} -> {val}")

def listar_notas(notas, alunos, nrnotas):
    for i in range (nrnotas):
        print (f"nota: {notas[i][0]}")
        print (f"aluno: {alunos[notas[i][1]["nome"]]}")

def menu():
    op = input("opções: 1- adicionar 2- listar 3- pesquisar 4- editar 5- sair")
    return op

def main():
    MAX_ITEMS = 100
    alunos = np.empty(MAX_ITEMS,dtype=object)
    pos = 0
    forma = (MAX_ITEMS,2)
    notas = np.zeros(forma, "i")
    nrnotas = 0

    #adicionar alunos
    while True:
        op = menu()
        if pos == MAX_ITEMS:
            print ("nao temos espaço disponivel: ")
            continue
        if op ==  "1":
            alunos[pos]= adicionar_aluno()
            pos += 1
        if op == "2":
            listar_alunos(alunos, pos)
        if op == "3": 
            aluno = procurar_aluno(alunos, pos)
            if aluno is not None:
                print (aluno)
            else: 
                print ("o aluno nao existe")
            
        if op == "4":
            aluno = procurar_aluno(aluno, pos)
            if aluno is not None:
                aluno["nome"] = input ("insira o nome que quer para o aluno: ")
                aluno["idade"] = input ("insira a idade que quer para o aluno: ")
                aluno["morada"] = input ("insira a morada que quer para o aluno: ")
                aluno["email"] = input ("insira o email que quer para o aluno: ")
        elif op == "5":            
            posicao = procurar_posição(alunos, pos)
            if procurar_posição(alunos, pos) is None:
                print ("nao")
            else:
                nota = int(input("insira a nota"))
                notas[nrnotas][0] = nota
                notas[nrnotas][1] = posicao
                nrnotas += 1

        elif op == "6":
            break
    
if __name__ == "__main__":
    main()