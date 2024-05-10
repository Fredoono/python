"""ler 10 nomes do utilizador e guardar no ficheiro"""
#abrir o ficheiro
with open("Nomes.txt","w",encoding="utf-8") as ficheiro:
    for i in range (10):
        nome = input("insira o nome da pessoa que quer adicionar:")
        ficheiro.write(f"{nome}\n")
    print ("dados guardados com sucesso")