#Exercicio_listas_1.py
#a
lista = []
MAXa = 5
contar = 0
for i in range (MAXa):
    n = int(input("insira um numero: "))
    lista.append(n)
    contar += n
print (lista)
print (f"a média é {(contar/MAXa)}")
#b
listab = []
Maxb = 10
positivos = 0
negativos = 0
for i in range(Maxb):
    n = float(input("insira um numero: "))
    listab.append(n)
    if n >= 0:
        positivos += 1
    else:
        negativos +=1
for i in range(Maxb-1,-1,-1):
    print (listab[i])
print (f"a percenteagem de numeros positivos é {positivos/len(listab)*100}%")
