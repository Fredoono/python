"""9.Fazer um programa para gerir os contactos de uma agenda.
 Deve permitir adicionar nome e telefone de cada contacto. 
 Deve permitir listar todos e pesquisar por um nome. Deve permitir Alterar o telefone de um nome."""
import numpy as np
contactos = np.zeros((100,2),"U20")
def menu(arr):
    pos = 0
    while True:
        print ("")
        print ("insira 1 caso queira inserir um contacto")
        print ("insira 2 caso ver a lista de todos os nomes")
        print ("insira 3 caso queira pesquisar por uma pessoa")
        print ("insira 4 caso queira mudar um contacto")
        print ("insira terminar para terminar")
        escolha = input("insira o numero correspondente: ")
        if escolha == "1":
            inserir_numero(arr,pos)
            pos +=1
        elif escolha == "2":
             listar_nomes(arr,pos)
        elif escolha == "3":
            procurar_nomes(arr)
        elif escolha == "4":
            mudar_contactos(arr)
        elif escolha == "terminar":
            break
        else:
            print ("erro, dados inválidos, tente denovo")
def inserir_numero(arr,pos):
    nome = input("insira o nome do contacto: ")
    arr[pos,0] = nome
    numero = input("insira o nome do contacto: ")
    arr[pos,1] = numero
def listar_nomes(arr,pos):
    for i in range(pos):
        print (f"nome: {arr[i,0]}")
        print (arr[i,1])
def procurar_nomes(arr):
    while True:
        escolha = input("use 1 para procurar por um numero atravez de um nome /n dijite 2 para procurar por um nomer atravez de um numero")
        nome = input("insira o nome que quer procurar: ")
        if escolha == "1":
            for i in range (arr.shape[0]):
                if arr[i,0] in nome:
                    print(f"o número de {arr[i,0]} é: {arr[i,1]}")
            if nome is not arr:
                print ("nao existe esse contacto")

        if escolha == "2":
            for i in range (arr.shape[0]):
                if arr[i,1] in nome:
                    print(f"o número de {arr[i,1]} é: {arr[i,0]}")
                    break                        
            if nome is not arr:
                print ("nao existe esse contacto")
        else:
            print ("dados inválidos")
def mudar_contactos(arr):
    while True:
        print ("escolha 1 para procurar um contacto pelo nome para mudar o seu número: ")
        print ("escolha 2 para procurar um contacto pelo numero para mudar o seu nome: ")
        print ("escolha 3 para procurar um contacto pela sua ordem de criação para mudar o nome e número: ")
        escolha = input("insira a sua escolha: ")
        if escolha == "1":
            nome = input("insira o nome da pessoa que quer procurar")
            for i in range (arr.shape[0]):
                if arr[i,0] == nome:
                    numero = input("insira o novo numero que deseja para esta pessoa: ")
                    arr[i,1] = numero
                escolha2 = input("imprima 1 se quiser alterar o numero do contacto, 0 se nao quiser alterar: ")
                if escolha2 == 1:
                    nome = input ("escolha o nome do contacto: ")
                    arr[i,1] = nome
                else:
                    break
            if nome is not arr:
                print ("nao existe esse contacto")
        if escolha == "2":
            numero = input("insira o nome da pessoa que quer procurar")
            for i in range (arr.shape[0]):
                if arr[i,1] == numero:
                    numero = input("insira o novo nome que deseja para esta pessoa: ")
                    arr[i,0] = numero
                escolha2 = input("imprima 1 se quiser alterar o numero do contacto, 0 se nao quiser alterar: ")
                if escolha2 == 1:
                    nome = input ("escolha o numero do contacto: ")
                    arr[i,0] = nome
                else:
                    break
            if numero is not arr:
                print ("nao existe esse contacto")
        if escolha == "3":
            while True:
                numero = int(input("insira o numero da data de criação do contacto: "))
                if numero < 0 or numero > 100:
                    continue
                escolha = input ("dijite 1 para alterar o nome, dijite 2 para alterar o numero, dijite 3 para alterar os dois")
                if escolha == "1" or escolha == "3":
                    nome = input ("insira o nome que quer para este contacto: ")
                    arr[numero,0] = nome
                if escolha == "2" or escolha == "3":
                    nome = input ("insira o numero que quer apra este contacto: ")
                    arr[numero,1] = nome
                break
menu(contactos)