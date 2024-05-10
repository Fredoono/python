#Implemente uma função que faz a rotação dos elementos de uma lista n posições para a esquerda. 
#Por exemplo, para a lista [1, 2, 3, 4, 5] e n = 2, o resultado deve ser [3, 4, 5, 1, 2].
lista = [1,2,3,4,5]
def emporrar(lista):
    num = int(input("insira um numero"))
    for i in range(num):
        pos = lista[0]
        lista.remove(pos)
        lista.insert(len(lista),pos)
emporrar(lista)
print(lista)