"""programa que le um inteiro de um ficheiro binario"""
import struct

with open("int.bin","rb") as ficheiro:
    temp=ficheiro.read(4)
    numero = struct.unpack("i",temp)[0]

print (numero)