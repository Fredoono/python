"""programa que le todos os ficheiros inteiros de um programa"""
import struct


with open("ints.bin","rb") as ficheiro:
    while True:
        temp=ficheiro.read(4)
        if not temp:
            break
        numero = struct.unpack('i',temp)[0]
        print (numero)
    posição = int(input("qual o nº a ler? "))
    #calcular a posição a ler sabendo que cada inteiro corresponder a 4 bytes
    posição = (posição-1)*4
    ficheiro.seek(posição)
    temp = ficheiro.read(4)
    numero = struct.unpack('i',temp)[0]
    print (numero)

