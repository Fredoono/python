import numpy as np
matriz1= np.array([[10,11],[10,11],[8,6]])
matriz2= np.array([[3,12],[13,12],[2,10]])

def SomaMatriz(arr1,arr2):
    arrSoma = np.empty((arr1.shape[0],arr1.shape[1]),"i")
    for i in range (arr1.shape[0]):
        for f in range (arr1.shape[1]):
            arrSoma[i,f] = arr1[i,f] + arr2[i,f]
    return arrSoma
    




print(SomaMatriz(matriz1,matriz2))