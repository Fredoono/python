import os
#verificar se o ficheiro existe
if os.path.exists("Nomes.txt")==False:
    print ("O ficheiro nao foi encontrado")
else:
    #abrir o ficheiro
    with open("Nomes.txt","r",encoding="utf-8") as ficheiro:
        while True:
            #ler a linha do ficheiro
            texto = ficheiro.readline()
            #verificar se chegamos no final
            if not texto:
                break
            print (texto,end="")