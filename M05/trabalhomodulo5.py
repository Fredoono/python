'''
PSI - Módulo 5
Estruturas de Dados Compostas
Coleções
'''

# Estrutura de dados
Disciplina_PSI={
                  'Modulos': ('Algoritmia','Estruturas de Controlo','Funções','Estruturas de Dados Estáticas'),
                  'WebGrafia':{'3wschool.com','github.com/alunosnet','udacity.com'} ,
                  'Aulas':['M1','M1','M1','M2','M2','M3','M3','M4','M4','M4','M4'],
                  'Avaliação':['Teste Escrito','Teste prático','Teste prático','Teste prático']
               }

# Mostrar os sites recomendados para a disciplina (webgrafia)
print (Disciplina_PSI["WebGrafia"])

# Mostrar o nome de um módulo pela posição (pedir ao utilizador)
pos = int(input("insira a posição desejada: "))
print (f" a aula foi de {Disciplina_PSI["Aulas"][pos]}")

# Mostrar as aulas que são dadas num módulo (pedir ao utilizador o nº do módulo)
num = input("insira numero do mudulo: ")
num = "M" + num
contar = 0
for i in range(len(Disciplina_PSI['Aulas'])):
    if num == Disciplina_PSI["Aulas"][i]:
        contar += 1
        modulo = Disciplina_PSI["Aulas"][i]
if contar > 0:
    print (F"{modulo} "*contar)
else:
    print ("nao foi encontrada aulas com esse modulo, tente verificar se utilizou o modulos correto.")

# Mostrar os módulos que tenham determinado conteudo (pedir ao utilizador)
palav = input("insira o conteudo que deseja procurar: ")
texto = ""
for i in range(len(Disciplina_PSI["Modulos"])):
    if palav.lower() in Disciplina_PSI["Modulos"][i].lower():
        texto += f"{Disciplina_PSI["Modulos"][i]}, "
texto += "são alguns dos conteudos."

# Mostrar os módulo cuja avaliação não é 'Teste Escrito'
for i in range (len(Disciplina_PSI["Avaliação"])):
    if Disciplina_PSI["Avaliação"] != "Teste Escrito":
        print (f"mudolo {i+1} não teve avaliação por teste escrito")

# Mostrar o nº de módulos da disciplina
print(f"são {len(Disciplina_PSI['Modulos'])} modulos")

# Adicionar mais 5 aulas do módulo M2
numer = 5
for i in range (numer): 
    Disciplina_PSI["Aulas"].append("M2")

# Adicionar uma chave nova para classificacoes que deve corresponder a uma lista de 4 notas indicadas pelo utilizador
notas = ""
for i in range (4):
    palavra = input("insira o que quer nas classificações: ")
    notas += f"{palavra} "
Disciplina_PSI["classificacoes"]= {"notas":(notas)}
print (Disciplina_PSI["classificacoes"])