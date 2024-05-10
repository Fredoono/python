sporting = []
benfica =[]
def adicionar(lista):
    while True:
        novo = input("insira o novo sócio do clube se nao quiser adicionar mais ninguém de um enter vaziu: ").capitalize()
        if novo != "":
            lista.append(novo)
        else:
            print ("concluído")
            break
def comparar(lista1,lista2):
    for i in range (len(lista1)-1,-1,-1):
        if lista1[i] in lista2:
            lista2.remove(lista1[i])
            lista1.remove(lista1[i])
            lista1.pop(i)

def main():
    adicionar(sporting)
    adicionar(benfica)
    comparar(sporting,benfica)
    print ((sporting))

if __name__ == "__main__":
    main()