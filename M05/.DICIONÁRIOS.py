dicionario_do_fred = {"nome":"fred","idade":30, "cidade":"viseu"}
print(dicionario_do_fred["nome"])
#para criar um chave nova é
dicionario_do_fred["altura"] = "180 :D"

meu_dicionario = {"nome" : 'Joaquim', 'nif' : '123123123', 'morada':'viseu'}
chaves = meu_dicionario.keys() #mostra as chaves
print(chaves)
valores = meu_dicionario.values() #mostra os valores das chaves
print(valores)
elementos = meu_dicionario.items() #mostra todas as chaves e os seus valores
print(elementos)

meu_dicionario.pop("nome")
print(meu_dicionario)