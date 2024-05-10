paises = {"Portugal":"Lisboa","Espanha":"Madrid","Alemanhã":"Berlim","Brazil":"Brazilia","França":"Paris"}
for pais,capital in paises.items():
    print (f"a capital de {pais} é {capital}")
while True:
    op = input("quer adicionar um novo pais? (reposta S/N) ")
    if op == "s" or op == "S":
        nome = input("insira o nome do pais: ")
        capital = input("insira a capital do pais: ")
        paises[nome]=capital
    else:
        break
# o utilizador insere um nome e nós damos a capital e vice versa
while True:
    op = input("deseja procurar por uma capital? (S/N): ")
    if op == "s" or op == "S":
        pais = input("qual pais deseja procurar? ")
        capital = print (paises.get("esse país nao existe."))
        print (capital)
    else:
        break
while True:
    op = input ("deseja procurar um país? ")
    if op == "S" or op == "s":
        capit = input("qual capital deseja procurar? ")
        if capital not in paises.values():
            print ("nao existe esta capital.")
        else:
            for chave, valor in paises.items():
                if valor == capit:
                    print (chave)
    else:
        break
        

print (paises)