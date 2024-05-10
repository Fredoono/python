"""o joaquim tem um restaurante com mesas de diferentes lotações (2,4,6 lugares) 
menu- opção 1- entrada de clientes , qual a mesa e quantas pessoas são (se a mesa estiver ocupada avisa)
    - opção 2 - saída de clientes
    - opção 3 terminar o programa
    mostrar o estado de todas as mesas
"""
import numpy as np
def configuração_de_mesas():
    mesas = int(input("quantas mesas tem o restaurante: "))
    qmesas = np.zeros(mesas,"i")
    for i in range (mesas):
        qmesas[i] = input (f"quantos lugares tem a mesa {i+1}: ")
    return (qmesas)
def menu(arr):
    lotação = np.empty (len(arr), "i")
    for i in range (len(arr)):
        lotação[i] = arr[i]
    while True:
        print ("ecolha opção 1 (entrar clientes), 2 (sair clientes), 3 (terminar o programa), 4 (mostrar o estado de todas as mesas)")   
        op = int(input("escolha a opção: "))
        if op == 1:
            mesa = int(input("escolha a mesa que quer editar: "))
            mesa = mesa - 1
            if arr[mesa] > 0:
                pessoas = int(input("quantas pessoas entram: "))
                if arr[mesa] >= pessoas:
                    arr[mesa] -= pessoas
                else: 
                    print (f"não á lugares suficientes na mesa {mesa+1}")
            else:
                print (f"não á lugares suficientes na mesa {mesa+1}")
        
        if op == 2:
            while True:
                mesa = int(input("escolha a mesa que quer em que saiam todos: "))
                mesa = mesa - 1
                if arr[mesa] == lotação[mesa]:
                    print ("mesa vazia")
                arr[mesa] = lotação[mesa]
            
        if op == 3:
            totalpessoas = 0
            for i in range (len(arr)):
                if arr[i] == lotação[i]:
                    print (f"a mesa {i+1} está totalmente livre")
                    totalpessoas = totalpessoas + arr[i]
                    
            for i in range (len(arr)): 
                if arr[i] == 0:
                    print (f"a mesa {i+1} está ocupada")
            print (f" o restaurante tem {totalpessoas} clientes no restaurante")
                
        if op == 4:
            break   

config_mesa = configuração_de_mesas()
menu(config_mesa)
        