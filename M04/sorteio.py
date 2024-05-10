#5 numeros e duas estrelas
import numpy as np 
import random 
numeros = np.empty(4,"i")
estrela = np.empty(2,"i")
def numeros_aliatórios(arr, máximo):
    indice = 0
    while True:
        aliatório = random.randint(1, máximo)
        if aliatório in arr:
            indice = indice
        else:
            arr[indice] = aliatório
            indice +=1
        if indice == len(arr): 
                #buble sort
            n = len(arr)
            for i in range(n):
                for j in range(0,n-i-1):
                    if arr[j] > arr[j+1]:
                        t = arr[j]
                    arr[j+1]=t
            return arr

print(numeros_aliatórios(numeros, 50))
print(numeros_aliatórios(estrela, 12))