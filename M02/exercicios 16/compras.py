dindin= float(input("insira o dinheiro que possui: "))
peso= float(input("insira o peso que pode carregar: "))
while True:
    print (f"tem {dindin} dinheiros e pode carregar {peso} kilos ")
    pesoP = float(input("insira o peso do produto"))
    dinP = float(input("insira o preço do produto"))
    if pesoP < peso and dinP < dindin:
        peso - pesoP 
        dindin - dinP
    elif pesoP > peso:
        print ("nao consegue suportar tanto peso")
    elif dinP > dindin:
        print ("nao tem dinheiro suficiente")
    
