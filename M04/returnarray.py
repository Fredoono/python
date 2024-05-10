import numpy as np
def ler_dados():
    numeros = np.empty(5,"i")
    for i in range (len(numeros)):
        numeros[i]= int (input("N"))
    return numeros
vetor = ler_dados()
print(vetor)
