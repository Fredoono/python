palavra = input("insira uma palavra")
lista = []
lista = palavra.split(" ")
copia = lista
for i in range(len(copia)):
    print (f"a palavra {lista[i]} aparece {lista.count(lista[i])} vezes")
