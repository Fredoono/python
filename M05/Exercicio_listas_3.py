#Exercicio_listas_3.py

lista = []
consoates = ""
for i in range (20):
    palavra = input("insira uma palavra com 20 letras: ")
    consoates += palavra
    lista.append(palavra)
vogais = "aeiou"
for palavra in lista:
    for letra in palavra:
        if letra not in vogais:
            print (letra)
maior_palavra = lista[0]
palavras_a = ""
for palavra in lista:
    if palavra > maior_palavra:
        maior_palavra = palavra
    if palavra[0] == "a":
        palavras_a += (f"{palavra} ")

print (f"a maior palavra é {maior_palavra}")
print (f"todas as palavras que comelam com a: {palavras_a}")