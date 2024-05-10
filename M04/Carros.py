"""
opções: 
1- entrada da matrícula de um carro
2- saída de um carro 
3- mostra a fila
4- terminar
máximo de 10 carros
"""
import numpy as np
Fila = np.zeros(10,"U8")
def menu():
    escolha = input("escolha a opção 1 para a entrada de um carro no fim da fila, a opção 2 para a saída do primeiro carro da fila, 3 para mostrar a fila e 4 para terminar o programa: ")
    return escolha

def entrada(Fila, ent):
    Fila[ent] = input ("insira a matrícula: ")
    return  # a fila nao altera mano :{ 
def saída(Fila):
    for i in range (len(Fila)-1):
        Fila[i] = Fila[i+1]
    Fila[9] = 0

def isfull(fila):
    comp = len(fila)
    if fila[comp-1] != "":
        return True
    else:
        return False
def main():
    ent = 0
    while True:
        if ent > 0:
            ent = 0
        cheio = isfull(Fila)
        opção = menu()
        if opção == "1" and cheio == False:
            entrada(Fila, ent)
            ent += 1
        elif opção == "2":
            saída(Fila)
            ent -= 1
        elif opção == "3":
            print (Fila)
        elif opção == "4":
            break
        else: print ("dados inválidos")
        
if __name__ == "__main__":
    main() 