import numpy as np
"""Precisamos de um programa para gerir as temperaturas médias mensais de um ano.
O programa dever ler as 12 temperaturas e depois mostrar o mês mais quente e mais frio.
Opcional: calcular e mostrar a temperatura média do ano e quantos meses tiveram temperatura superior à média"""

meses = np.array(["janeiro","fevereiro","março","abril","maio","junho","julho","agosto","setembro","outubro","novembro","dezembro"])
tempmeses = np.empty(12,dtype="f")
maior = 0
menor = 0

for pos in range (0,12,1):
    tempmeses[pos] = int(input(f"insira a temperatura do mês de {meses[pos]} : "))
    if pos == 0:
        maior = tempmeses[pos]
        menor = maior
    if tempmeses[pos] > maior:
        maior = tempmeses[pos]
    if tempmeses[pos] < menor:
        menor = tempmeses[pos]
print (f" o mês mais quente apresentou temperaturas de {maior}")
print (f" o mês mais frio apresentou temperaturas de {menor}")

def media(x):
    soma = 0
    for i in range (len(x)):
        soma = soma + x[i]
    return(soma/ len(x))

print (f"a média das temperaturas é {media(tempmeses)}")