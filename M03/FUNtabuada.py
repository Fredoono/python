def tabuada(num):
    for i in range (1,11):
        print (f"{i} vezes {num} = {i*num}")


numero = int(input("insira o numero que deseja ver a tabuada"))
tabuada(numero)