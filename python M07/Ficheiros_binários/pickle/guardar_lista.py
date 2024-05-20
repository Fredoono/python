import pickle

lista = []
nome = input("insira texto: ")
while nome != "":
    nome = input("insira texto: ")
    lista.append(nome)

with open('minha_lista.pkl','wb') as ficheiro:
    pickle.dump(lista,ficheiro)

with open('minha_lista.pkl','rb') as ficheiro:
    try:
        lista_nova = pickle.load(ficheiro)
    except EOFError:
        print ("o ficheiro parece estar vaziu")

print(lista_nova)