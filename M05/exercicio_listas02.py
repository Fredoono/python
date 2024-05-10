#Crie um programa que preenche uma lista com dez palavras totalmente aleatórias.
#Para gerar as palavras pode ser útil utilizar as funções chr(codigo) e codigo=ord(letra). 
#A primeira devolve uma letra com base no código ascii e a segunda devolve o código ascii da letra.
#No final deve listar as palavras.
import random
lista = []
for i in range (10):
    palavra = ""
    comprimento = random.randint(2, 15)
    for i in range (comprimento):
        nr = random.randint(97,122)
        palavra += (chr(nr))
    lista.append(palavra)
print (lista)