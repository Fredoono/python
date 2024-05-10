import numpy as np 
arr = np.zeros((10,10),"i")
def diagonais(arr,diagonal):
    for i in range (arr.shape[0]):
        arr[i,i] = diagonal
    print (arr)
diagonais(arr,1)