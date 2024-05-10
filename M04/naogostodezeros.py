import numpy as np
arr = np.array([[-2,2,-3],[16,-3,4]])
def removernegativos(arr):
    for i in range (arr.shape[0]):
        for f in range (arr.shape[1]):
            if arr[i,f] < 0:
                arr[i,f] = 0
    return arr
print(removernegativos(arr))