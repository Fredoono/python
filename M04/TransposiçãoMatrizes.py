import numpy as np
arr = np.array([[1,2],[3,4],[5,6]])
print (arr)
def TranposiçãoMatrizes(arr):
    arrdel = np.empty((arr.shape[1],arr.shape[0]),"i")
    for i in range (arr.shape[0]):
        for f in range (arr.shape[1]):
            arrdel[f,i] = arr[i,f]
    return arrdel

print (TranposiçãoMatrizes(arr))