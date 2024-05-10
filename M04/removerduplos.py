import numpy as np
vetor = np.array([1, 3, 4, 3, 4, 3, 4, 5, 2, 6])
def remover_duplicados(arr):
    temp = np.zeros(len(arr))
    posicao = 0
    for i in range (len(arr)):
        if arr[i] not in temp:
            temp[posicao] = arr[i]
            posicao +=1
    return temp
print(remover_duplicados(vetor))