"""programa para gravar strings em binário"""
import struct

quantidade = int(input("insira a quantidade de string a gravar: "))

with open("strings.bin","wb") as ficheiro:
    for i in range(quantidade):
        texto = input("insira um texto: ")
        dados = struct.pack("50s",texto.encode('utf-8'))
        ficheiro.write(dados)