import numpy as np
MAX_ITEMS = (6,2)
moedas = np.array([[0.01,0],[0.02,0],[0.05,0],[0.1,0],[0.2,0],[0.5,0],[1,0],[2,0]])
for linhas in range (moedas.shape[0]):
    quantidademoeda = int(input(f"insira quantas moedas do tipo {linhas} tem "))
    moedas[linhas,1] = quantidademoeda
print (moedas)
quantidadePagar = float(input("quantidade que tem de pagar: "))
dinheiroRecebido = float(input("quantidade de dinheiro recebido: "))
#da soma de tudo ver o quanto tem que pagar e calcular quantas moedas de cada necessárias para dar o troco
total = 0
for i in range (moedas.shape[0]):
    total += moedas[i,0] * moedas[i,1]
QTtroco = dinheiroRecebido - quantidadePagar
troco = np.array([[0.05,0],[0.1,0],[0.2,0],[0.5,0],[1,0],[2,0]])
print(QTtroco)
if QTtroco >0:
    for i in range (moedas.shape[0]):
        if moedas[i,1] == 0:
            continue
        while moedas[i,0] < QTtroco and moedas[i,1] > 0:
            print (QTtroco)
            print (moedas[i,0])
            troco[i,1] = troco[i,1] +1
            moedas[i,1] -= 1
            QTtroco = QTtroco - moedas[i,0]
print (troco)