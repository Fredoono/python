import pickle

dicionario = {'nome':'Fred',
              'idade':33,
              'email':'mimikyo@pokemon.com'}

NOME_FICHEIRO="dados.bin"

with open(NOME_FICHEIRO,"wb") as ficheiro:
    pickle.dump(dicionario,ficheiro)
    