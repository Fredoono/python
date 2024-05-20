import os
#listar os ficheiros e as pastas
ficheiros = os.listdir('.')
#listar todos
print(ficheiros)
#lista só ficheiros
for ficheiro in ficheiros:
    if os.path.isfile(ficheiro):
        print(ficheiro)

