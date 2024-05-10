import numpy as np
"agora com funções"
MAX = 5
cincoV1 = np.empty(MAX,dtype="i")
cincoV2 = np.empty(MAX,dtype="i")

#função para ler os dados
def ler_dados(numeros):
    for num in range (len(numeros)):
        numeros[num] = int(input("insira um numero"))

def somar_numeros(numeros):
    for num in numeros:
        soma= soma + num
    return soma


ler_dados(cincoV1)
ler_dados(cincoV2)

somar_numeros(cincoV1)
somar_numeros(cincoV2)