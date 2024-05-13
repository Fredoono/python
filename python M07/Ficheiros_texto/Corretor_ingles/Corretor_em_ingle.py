import os
frase = input("write here: ")
corret = True
retirar = ",!#?=.:;"
#verificar se o ficheiro existe
if os.path.exists("words.txt")==False:
    print ("file found")
else:
    #abrir o ficheiro
    with open("words.txt","r",encoding="utf-8") as ficheiro:
        words = []
        while True:
            text = ficheiro.readline()
            if not text:
                break
            words.append(text.strip("\n").lower())
    for letra in frase:
        if letra in retirar:
            frase = frase.replace(letra,"")

    palavras = frase.split()
    caracteres= []
    for palavra in palavras:
        if palavra.lower()not in words:
            print (f"that words  ({palavra}) is not in the dictionary {palavra}")
            corret = False
    if corret == True:
        print ("you know how to write :D")