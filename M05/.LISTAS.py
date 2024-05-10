#defenir
lista = [1,2,3,4]
#ficam indexados por posiçõest
print (lista [0])
#adicionar elemento
lista.append(111)
for x in lista:
    print (x)
#adicionar elemento no final
lista.insert(0,"tá tudo bem?")
#juntar listas
lista2 = [1,11,111,1111,11111]
junção = lista + lista2 
junção.pop(1)
print (junção)
lista_cidades=["Viseu","Tondela","Mangualde"]
lista_cidades.insert(0,"Lisboa")
print(lista_cidades)
nomes = "fred joaquim salada"
lista_nomes = nomes.split(" ")
print (lista_nomes)
soma = sum(lista2)
print (soma)