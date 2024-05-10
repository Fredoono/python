#Exercicio_listas_2.py
notas = []
maior = 0
soma = 0
positivos = 0
negativos = 0
for i in range(4):
    n = float(input("insira uma nota"))
    notas.append(n)
    soma += n
    if n > maior:
        maior = n
    if n >= 0:
        positivos += 1
    else:
        negativos +=1
print (f"a média é {soma/len(notas)}, a maior nota é {maior}, a percentagem de positivas é {positivos/len(notas)*100}, a percentagem de negativos é {negativos/len(notas)*100}")
print (f"a maior nora é {max(notas)}")