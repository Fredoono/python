import struct

#numero a guardar
numero = 111
#abrir o arquivo para escrita binária
with open("int.bin","wb") as ficheiro:
    #empacotar o número no formato escolhido e escrever no arquivo
    temp=struct.pack("i",numero)
    ficheiro.write(temp)