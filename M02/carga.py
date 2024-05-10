P = 0
while "Fred é fixe":
    print ("")
    print (f"peso atual {P}")
    print (f"peso atual {10000 - P}")
    m = int(input("insira 1 para carregar, 2 para descarregar, 3 para encerrar o programa- "))
    if m == 1:
        p = int(input("insira quanto quer carregar do caminhão em Kg: "))
        P = P +p
        if P > 10000:
            P = P - p
            print ("carga exessiva, insira outro valor: ")
    elif m == 2:
        pm = int(input("insira quanto quer remover em Kg: "))
        P = P - pm
        if P > 10000 or P < 0:
            P = P + pm
            print ("erro nao tem quantidade suficiente pra remover, insira outro valor")
    elif m == 3:
            break
    else:
            print ("dados inválidos")   