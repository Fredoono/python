import numpy as np
numeros = np.empty(4,dtype="i")
numeros0 = np.empty(4,dtype="i")
var = len(numeros0)-1
for i in range (len(numeros)):
    numeros[i] = int(input("mete um numero aqui: "))
for i in range (len(numeros)):
    numeros0[i] = numeros[var]
    var = var -1
print (numeros0)