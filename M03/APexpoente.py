#quando uma função se chama a ela mesma
def Expoente(base,expoente):
    if expoente == 1:
        return base
    else:
        return base*Expoente(base,expoente-1)
    
print(Expoente(4,3))

