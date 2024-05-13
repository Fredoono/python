#Frederico Sousa 24585
import utils, os, datetime
nome_ficheiro = "tarefas.txt"

#adicionar tarefa
def criar_tarefa():
    tarefa = utils.le_texto("insira o nome da tarefa que deseja adicionar: ")
    descrição = utils.le_texto("insira uma descrição para a terfa que quer adicionar: ")
    data = utils.le_texto("insira a data de conclusão (dd/mm): ",5)

    Nova_tarefa = {"tarefa":tarefa,
                    "descrição":descrição,
                    "data":data
                   }
    return Nova_tarefa

def adicionar():
    tarefa = criar_tarefa()
    with(open(nome_ficheiro,"a",encoding="utf-8")) as ficheiro:
        ficheiro.write(f" - {tarefa["data"]} - {tarefa["tarefa"]} - {tarefa["descrição"]} \n")



#listar tarefas
def listar():
    """Função para listar as tarefas"""
    if os.path.exists(nome_ficheiro) == False:
        return
    with(open(nome_ficheiro,"r",encoding="utf-8")) as ficheiro:
        while True:
            linha = ficheiro.readline()
            if not linha:
                break
            tarefa = linha.split("-")
            print (f"{tarefa[2]} - {tarefa[3]} conclusão:{tarefa[1]}")
            print (tarefa[0])
            print ("-"*29)

#remover tarefas
def apagar():
    """função para apagar as tarefas"""
    if os.path.exists(nome_ficheiro) == False:
        return
    with(open(nome_ficheiro,"r",encoding="utf-8")) as ficheiro:
        with(open("temp.txt","w",encoding="utf-8")) as f_escrita:
            apagar = utils.le_numero("insira a linha que quer apagar: ")
            nr_linha = 0
            while True:
                linha = ficheiro.readline()
                nr_linha += 1
                if not linha:
                    break
                if nr_linha != apagar:
                    f_escrita.write(linha)
    #apagar o ficheiro
    os.remove(nome_ficheiro)
    os.rename("temp.txt",nome_ficheiro)
            
        
        
#marcar tarefa como concluída
def concluído():
    """função para concluír uma tarefa"""
    if os.path.exists(nome_ficheiro) == False:
        return
    with(open(nome_ficheiro,"r",encoding="utf-8")) as ficheiro:
        with(open("temp.txt","w",encoding="utf-8")) as f_escrita:
            concluído = utils.le_numero("insira a linha que quer concluír: ")
            nr_linha = 0
            while True:
                linha = ficheiro.readline()
                nr_linha += 1
                tarefa = linha.split("-")
                if not linha:
                    break
                if tarefa[0] == "[Concluído] ":
                    print ("esta tarefa já está concluída")
                    return
                if nr_linha == concluído :
                    f_escrita.write(f"[Concluído]{linha}")
                else:
                    f_escrita.write(linha)
    #apagar o ficheiro
    os.remove(nome_ficheiro)
    os.rename("temp.txt",nome_ficheiro)

def listar_concluídos():
    """Função para listar as tarefas concluídas"""
    if os.path.exists(nome_ficheiro) == False:
        return
    with(open(nome_ficheiro,"r",encoding="utf-8")) as ficheiro:
        while True:
            linha = ficheiro.readline()
            tarefa = linha.split("-")
            if not linha:
                break
            if tarefa[0] == "[Concluído] ":
                print (f"{tarefa[2]} - {tarefa[3]} conclusão:{tarefa[1]}")
                print (tarefa[0])
                print ("-"*29)
def listar_mes():
    """Função para listar as tarefas concluídas"""
    if os.path.exists(nome_ficheiro) == False:
        return
    with(open(nome_ficheiro,"r",encoding="utf-8")) as ficheiro:
        mes = utils.le_texto("insira o mes para listar as tarefas")
        while True:
            linha = ficheiro.readline()
            tarefa = linha.split("-")
            if not linha:
                break
            data = tarefa[1] 
            if data[4] ==  mes[0] and data[5] == mes[1]:
                print (f"{tarefa[2]} - {tarefa[3]} conclusão:{tarefa[1]}")
                print (tarefa[0])
                print ("-"*29)

def main():
    while True:
        op=utils.menu("Ficheiros Texto",["Adicionar","Listar","Apagar","concluir","listar só concluidos","listar tarefas para ser concluídas este mes","Terminar"])
        if op==1:
            adicionar()
        if op==2:
            listar()
        if op==3:
            apagar()
        if op == 4:
            concluído()
        if op == 5:
            listar_concluídos()
        if op == 6:
            listar_mes()
        if op == 7:
            break

main()