"""programa para gravar string em binário"""
import struct

texto = input("insira o seu nome: ")

with open("string.bin","wb") as ficheiro:
    dados = struct.pack("50s",texto.encode('utf-8'))
    ficheiro.write(dados)