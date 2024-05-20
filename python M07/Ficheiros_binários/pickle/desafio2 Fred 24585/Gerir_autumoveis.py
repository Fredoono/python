#modulo principal realizado por Frederico Sousa 10ºT nº8 2024
import os, pickle
import utils
Nome_ficheiro = 'veículos.pkl' 
DATA_ATUAL = 2024
#deve adicionar veiculos (matricula, marca, modelo ano de fabrico)
def adicionar():
    veículo = []
    matricula = utils.lersotexto("insira a matrícula do veículo: ")
    marca = utils.lersotexto("insira a marca do veículo: ")
    modelo = utils.lersotexto("insira o modelo do veículo: ")
    ano = utils.lersonumeros("insira o ano de fabrico: ")
    veículo.append(matricula)
    veículo.append(marca)
    veículo.append(modelo)
    veículo.append(ano)
    #adicionar ao ficheiro binário
    with open(Nome_ficheiro,'ab') as ficheiro:
        pickle.dump(veículo,ficheiro)



#listar veículos

def listar():
    """função que lista todos os carross"""
    if os.path.exists('agenda.bin') == False:
        print("ficheiro nao encontrado")
        return
    with open(Nome_ficheiro,'rb') as ficheiro:
        while True:
            try:
                Veículo = pickle.load(ficheiro)
                print (f"matrícula: {Veículo[0]}, marca: {Veículo[1]}, modelo: {Veículo[2]}, ano de fabrico: {Veículo[3]} ")
            except EOFError:
                print ("-----------fim-----------")
                break

#pesquisar veículos
def pesquisar():
    if os.path.exists('agenda.bin') == False:
        print("ficheiro nao encontrado")
        return
    marca = utils.lersotexto("insira a marca que deseja procurar: ")
    Todos_veículos = []
    #guardar dados
    with open(Nome_ficheiro,'rb') as ficheiro:
        while True:
            try:
                Veículo = pickle.load(ficheiro)
                Todos_veículos.append(Veículo)
            except EOFError:
                break
    print (f"todos os veículos da marca {marca}: ")
    for veículo in Todos_veículos:
        if veículo[1] == marca:
            print (f"matrícula: {veículo[0]}, modelo: {veículo[2]}, ano de fabrico: {veículo[3]}")


#remover veículos
def remover():
    if os.path.exists('agenda.bin') == False:
        print("ficheiro nao encontrado")
        return
    matricula = utils.lersotexto("insira a matricula do veículo que deseja apagar: ")
    removidos = 0
    Todos_veículos = []
    #guardar dados
    with open(Nome_ficheiro,'rb') as ficheiro:
        while True:
            try:
                Veículo = pickle.load(ficheiro)
                Todos_veículos.append(Veículo)
            except EOFError:
                break
    #apagar
    with open(Nome_ficheiro,'wb') as ficheiro:
        for veículo in Todos_veículos:
            if veículo[0] == matricula:
                removidos +=1
            else:
                pickle.dump(veículo,ficheiro)
    print (f"foram removidos {removidos} veículos")


def pesquisar_anos():
    """função que mostra todos os carros construídos á mais de 10 anos"""
    if os.path.exists('agenda.bin') == False:
        print("ficheiro nao encontrado")
        return
    desanos= DATA_ATUAL-10
    Todos_veículos = []
    #guardar dados
    with open(Nome_ficheiro,'rb') as ficheiro:
        while True:
            try:
                Veículo = pickle.load(ficheiro)
                Todos_veículos.append(Veículo)
            except EOFError:
                break
    #listar
        for veículo in Todos_veículos:
            if veículo[3] < desanos:
                print(f"matrícula: {veículo[0]}, marca: {veículo[1]}, modelo: {veículo[2]}, ano de fabrico: {veículo[3]} ")


def melhor_marca():
    """Função que mostra a marca com mais carros existentes"""
    if os.path.exists('agenda.bin') == False:
        print("ficheiro nao encontrado")
        return
    maior_valor=0
    maior_marca =""
    marcas = {}
    Todos_veículos = []
    #guardar dados
    with open(Nome_ficheiro,'rb') as ficheiro:
        while True:
            try:
                Veículo = pickle.load(ficheiro)
                Todos_veículos.append(Veículo)
            except EOFError:
                break
    for veículo in Todos_veículos:
        marcas[veículo[1]] = 0
    for veículo in Todos_veículos:
        marcas[veículo[1]] += 1
    for chave,valor in marcas.items():
        if valor > maior_valor:
            maior_valor = valor
            maior_marca = chave
    print(f"a marca com mais veículo é {maior_marca}")


def main():
    """função principal"""
    while True:
        utils.menu_maker("menu",["adicionar","listar","pesquisar","remover","listar os veículos com mais de 10 anos","mostrar a marca com mais carros","terminar"],"=")
        op = utils.lersonumeros("opção: ")
        if op == 1:
             adicionar()
        elif op == 2:
            listar()
        elif op == 3:
            pesquisar()
        elif op == 4:
            remover()
        elif op == 5:
            pesquisar_anos()
        elif op == 6:
            melhor_marca()
        else:
            break

if __name__ == "__main__":
    main()