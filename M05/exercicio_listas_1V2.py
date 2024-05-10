lista = []
MAXa = 5
contar = 0
n = (input("insira todos os numeros com espaços em branco"))
lista= n.split(" ")
#lista = [int(x) for x in lista]
for i in range(len(lista)):
    lista[i] = int(lista[i])
contar = sum(lista)
print (f"a média é {(contar/MAXa)}")
lista = [int(x) for x in lista]