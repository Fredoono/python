import pickle

NOME_FICHEIRO="dados.bin"

with open(NOME_FICHEIRO,"rb") as ficheiro:
    while True:
        try:
            dicionario = pickle.load(ficheiro)
            print (dicionario)
        except EOFError:
            break
print(dicionario)