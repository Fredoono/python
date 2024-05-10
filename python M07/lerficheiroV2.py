"""programa que le um ficheiro de texto"""
#abrir o ficheiro pra leitura, o ficheiro feicha-se automáticamente
with open("Meu_ficheiro.txt","r",encoding="utf-8") as ficheiro:
    #ler o conteúdo
    texto = ficheiro.read()
#mostrar
print (texto)