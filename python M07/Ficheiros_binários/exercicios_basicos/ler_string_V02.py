"""programa que le uma string"""
import struct

with open('strings.bin','rb') as ficheiro:
    while True:
        temp = ficheiro.read(50)
        if not temp:
            break
        texto  = struct.unpack('50s', temp)[0]
        texto_limpo= texto.decode('utf-8').rstrip('\x00')
        print (texto_limpo)
    posição = int(input("qual o texto a ler: "))
    posição = (posição-1)*50
    ficheiro.seek(posição)
    temp = ficheiro.read(50)
    numero = struct.unpack('50s',temp)[0]
    numero = numero.decode('utf-8').rstrip('\x00')
    print (numero)