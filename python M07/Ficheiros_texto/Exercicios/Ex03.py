"""um programa que remove os nomes remetidos de Nomes.txt"""
import os
#verificar se o ficheiro existe
if os.path.exists("Nomes.txt")==False:
    print ("O ficheiro nao foi encontrado")
else:
    #abrir o ficheiro
    with open("Nomes.txt","r+",encoding="utf-8") as ficheiro:
        nomes = []
        while True:
            texto = ficheiro.readline()
            if not texto:
                break
            if not texto.strip("\n") in nomes:
                nomes.append(texto.strip("\n"))
    with open("Nomes.txt","w",encoding="utf-8") as ficheiro:
        for nome in nomes:
            ficheiro.write(f"{nome}\n")
    print ("dados alterados com sucesso")