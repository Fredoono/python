#exercicio 1
meses_do_ano= ("janeiro","fevereiro","marco","abril","junho","julho","aagosto","setembro","otubro","novembro","desembro")
#exercicio 2
print (meses_do_ano[2])
#exercicio 3
verao = meses_do_ano[5:8]
print (verao)
#exercicio 4
if "junho" in meses_do_ano:
    print(True)
else:
    print (False)
#exercicio 5  
cores_primarias = ("Vermelho", "Verde", "Azul")
cores_secundarias = ("Laranja", "Violeta", "Amarelo")
juncaocores =(cores_primarias+cores_secundarias)
#exercicio 6
for i in range (2):
    print (juncaocores)
#exercicios 7
amigos = 111,12,11,11,112,100
#exercicio 8
for i in range (len(juncaocores)):
    if "Verde" in juncaocores[i]:
        print (f"o indice da primeira ocorrencia de verde é {i}")
#exercicio 9
contar = 0
for i in range(len(juncaocores)):
    for f in range(len(juncaocores[i])):
        if "a" == juncaocores[i][f] or "A" == juncaocores[i][f]:
            contar += 1
print (contar)
#exercicio 10
amigos_ordenados = sorted(amigos)
print(amigos_ordenados)

"""hacker"""
def soma (tuplo):
    contar = 0
    for i in range (len(tuplo)):
        contar += tuplo[i]
    return contar
print (soma(amigos))

def maiorpalavra(tuplo):
    maior_palavra = tuplo[0]
    for i in range (len(tuplo)):
        if len(tuplo[i]) > len(maior_palavra):
            maior_palavra = tuplo[i]
    return maior_palavra
print (maiorpalavra(juncaocores))
import numpy as np
def médiapar():
    contar = 0
    pare = 0
    qt= int(input("quantos numeros quer? "))
    arr = np.zeros(qt,"i")
    for i in range (qt):
        numero = int(input("insira o número: "))
        arr[i] = numero
    tuplo = tuple(arr)
    for i in range(len(tuplo)):
        if tuplo[i] % 2 == 0:
            contar += tuplo[i]
            pare += 1
    return (contar/pare)
print (médiapar())