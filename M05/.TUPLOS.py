#é basicamente um array mas nao pode ser alteravel
meu_tuplo=(1,2,3)
print (meu_tuplo)
outro_tuplo = (("ford","fiesta","azul"),("ferrari","f40","azul"),("bmw","m4","branco"),("vw","polo","azul"))
print (outro_tuplo)
print(outro_tuplo[0].count("azul"))
if "azul" in outro_tuplo:
    print ("tem azul no tupolo")
