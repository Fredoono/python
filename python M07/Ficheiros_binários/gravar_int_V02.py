"""guarda varios numero inteiros"""
import struct

#numeros a guardar
quantidade = int(input("quantos inteiros quer quardar?"))

#abrir o arquivo para escrita binária
with open("ints.bin","wb") as ficheiro:
    for i in range(quantidade):
        numero = int(input("insira um numero"))
        temp = struct.pack("i",numero)
        ficheiro.write(temp)
    #perguntar a posição do numero
