frase = input("insira a frase desejada")
frase = frase.lower()
frase =frase.strip()
frase += " "
dic = {}
palavra = ""
for i in frase:
    if i != " ":
        palavra = palavra + i
    else:
        if palavra in dic:
            dic[palavra] += 1
        else:
            dic[palavra] = 1
        palavra = ""
print (dic)
        
