import os

def listar_ficheiros(caminho):
    ficheiros = os.listdir(caminho)
    print (ficheiros)
    for ficheiro in ficheiros:
        if not os.path.isfile(os.path.join(ficheiro)):
            listar_ficheiros(os.path.join(ficheiro))