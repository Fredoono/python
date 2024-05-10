"""
Sets automáticamente removem duplicados
Não ordenados
pode se adicionar ou remover uma das váriaveis nele
nao pode ter elementos imutaveis (nao pode ter listas)
"""
nomes_1 = {"joaquim", "Ana", "Dan", "manuel", "miguel"}
nomes_2 = {"Fredoono", "jonas", "gabriel", "josé", "Ana"}
união = nomes_1.union(nomes_2)
print(união)
diferença = nomes_1.difference(nomes_2)
print (diferença)
interceção = nomes_1.intersection(nomes_2)
print (interceção)
nomes_1.add("pai natal")
if "pai natal" in nomes_1:
    print ("O PAI NATAL É REAL")
else:
    print ("mata todas as bruxas")
nomes_1.remove("pai natal")
print (nomes_1)