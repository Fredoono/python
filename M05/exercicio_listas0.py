#1. Crie duas listas com nomes de sócios de dois clubes de futebol inseridos pelo utilizador.
Braga = []
Porto = []
def adicionar_sócios(lista):
    while True:
        n = input("insira um socio de futebol pra esta equipa: ")
        if n == "":
            break
        else:
            lista.append(n)
adicionar_sócios(Braga)
adicionar_sócios(Porto)

#2. Compare as duas listas e coloque numa terceira listas os nomes que são comuns aos dois clubes.
junção = []
def intersecao_de_listas(lista1,lista2,jun):
    for i in range (len(lista1)):
        if lista1[i] in lista2:
            jun.append(lista1[i])
intersecao_de_listas(Braga,Porto,junção)
print (junção)

#3. Para cada nome da terceira lista solicite ao utilizador em qual clube pretende permanecer e de acordo com a escolha deve remover o nome do outro clube.
for i in range (len(junção)):
    escolha = (input(f"escolha 1 para o jogador {junção[i]} para remove-lo de Braga e 2 para remove-lo do Porto"))
    if escolha == "1":
        Braga.remove(junção[i])
    elif escolha == "2":
        Porto.remove(junção[i])

#4. No final deve listar ordenar as três listas e mostrar os nomes ao utilizador
Braga = sorted(Braga)
Porto = sorted(Porto)
junção = sorted(junção)
def mostrar_ao_utilizador(lista):
    for i in range (len(lista)):
        print (lista[i])
    print ("#"*25)
mostrar_ao_utilizador(Braga)
mostrar_ao_utilizador(Porto)
mostrar_ao_utilizador(junção)