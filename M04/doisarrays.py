import numpy as np
MAX = 5
cincoV1 = np.empty(MAX,dtype="i")
cincoV2 = np.empty(MAX,dtype="i")

for num in range (MAX):
    numero = input ("insira um numero para o vetor")
    cincoV1[num] = numero

for num in range (MAX):
    cincoV2[ num ] = int(input("insira um numero"))

soma1 = 0 
soma2 = 0 
for num in range (MAX): 
    soma1 = soma1 + cincoV1[num]
    soma2 = soma2 + cincoV2[num]
#depois faz isto com funções