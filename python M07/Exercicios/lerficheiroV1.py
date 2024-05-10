""""programa para ler um ficheiro de texto"""
#abrir o ficheiro
ficheiro = open("Meu_ficheiro.txt","r")
#ver conteudo do ficheiro
texto = ficheiro.read()
#fechar o ficheiro
ficheiro.close()
#mostrar
print (texto)