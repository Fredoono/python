"""programa que le uma string"""
import struct

with open('string.bin','rb') as ficheiro:
    dados = ficheiro.read(100)
    texto  = struct.unpack('50s', dados)[0]
    texto_limpo= texto.decode('utf-8').rstrip('\x00')

print (texto_limpo)