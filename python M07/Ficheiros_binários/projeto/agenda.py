"""programa apra gerir uma agenda de contactos num ficheiro binário
binarios
    funcionalidades:
        -adicionar um co0ntacto
        -editar
        -remover
    dados: nome (100b), idade(4b), email(64b), Telefone (9b) 
    no total são 177 bytes
"""
import struct, os

def adicionar():
    """função que adicionar um novo contacto"""
    nome = input("insira o nome do usuário/a ")
    idade = int(input("insira a idade do usuário/a "))
    email = input("insira o email do usuário/a ")
    telefone = input("insira o telefone do utilizador/a ")
    with open("agenda.bin","ab") as ficheiro:
        nome = struct.pack("100s",nome.encode('utf-8'))
        idade = struct.pack("i",idade)
        email = struct.pack("64s",email.encode('utf-8'))
        telefone = struct.pack("9s",telefone.encode('utf-8'))
        ficheiro.write(nome)
        ficheiro.write(idade)
        ficheiro.write(email)
        ficheiro.write(telefone)

def remover():
    """função que remove um contacto"""
    if os.path.exists('agenda.bin') == False:
        return
    nome_remover = (input("Qual o nome do contacto a editar:"))
    with open("agenda.bin","rb") as ficheiro:
        with(open("temp.txt","wb")) as f_escrita:
            while True:
                temp = ficheiro.read(177)
                if not temp:
                    break
                nome = struct.unpack('100s77s', temp)[0]
                nome = nome.decode('utf-8').rstrip('\x00')
                if nome != nome_remover:
                    # nome = struct.pack("100s",nome.encode('utf-8'))
                    # f_escrita.write(nome)
                    # temp = ficheiro.read(77)
                    f_escrita.write(temp)
    os.remove('agenda.bin')
    os.rename("temp.txt",'agenda.bin')

def removerV2():
    if os.path.exists('agenda.bin') == False:
        return
    posição = int(input("qual a posição do contacto a remover?"))
    posição = (posição-1)*177
    registo = 0
    with open('agenda.bin') as ficheiro_leitura:
        with open("temp.bin","wb") as ficheiro_escrita:
            while True:
                dados = ficheiro_leitura.read(177)
                if not dados:
                    break
                if posição != registo:
                    ficheiro_escrita.write(dados)
                registo += 177
    os.remove('agenda.bin')
    os.rename("temp.txt",'agenda.bin')




def editar():
    posicao = int(input("Qual o nº do contacto a editar:"))
    posicao = (posicao - 1) * 177
    with open("agenda.bin","rb+") as ficheiro:
        ficheiro.seek(posicao)
        dados_binarios = ficheiro.read(177)
        if not dados_binarios:
            return
        nome, idade, email, telefone = struct.unpack("100si64s9s",dados_binarios)
        nome = nome.decode('utf-8').rstrip('\x00')
        email = email.decode('utf-8').rstrip('\x00')
        telefone = telefone.decode('utf-8').rstrip('\x00')
        print(f"{nome}\t{idade}\t{email}\t{telefone}")
        #novos dados do contacto
        nome=input("Nome:")
        idade=int(input("Idade:"))
        email=input("Email:")
        telefone=input("Telefone:")
        #posicionar no ficheiro
        ficheiro.seek(posicao)
        nome=struct.pack("100s",nome.encode("utf-8"))
        ficheiro.write(nome)
        idade=struct.pack("i",idade)
        ficheiro.write(idade)
        email=struct.pack("64s",email.encode("utf-8"))
        ficheiro.write(email)
        telefone=struct.pack("9s",telefone.encode("utf-8"))
        ficheiro.write(telefone)

def listar():
    if os.path.exists("agenda.bin")== False:
        return
    with open("agenda.bin","rb") as ficheiro:
        op = int(input("1- listar todos \n 2- listar contacto especifico"))
        if op == 1:
            while True:
                #nome
                temp = ficheiro.read(100)
                if not temp:
                    break
                nome = struct.unpack('100s', temp)[0]
                nome = nome.decode('utf-8').rstrip('\x00')
                print("="*25)
                print(nome)
                #idade
                temp = ficheiro.read(4)
                idade = struct.unpack('i',temp)[0]
                print (idade)
                #email
                temp = ficheiro.read(64)
                email = struct.unpack('64s', temp)[0]
                email = email.decode('utf-8').rstrip('\x00')
                print(email)
                #telefone
                temp = ficheiro.read(9)
                telefone = struct.unpack('9s', temp)[0]
                telefone = telefone.decode('utf-8').rstrip('\x00')
                print(telefone)

        if op == 2:
            contacto = int(input("insira o numero do contacto que quer listar"))
            contacto = (contacto-1)*177
            ficheiro.seek(contacto)
            #nome
            temp = ficheiro.read(100)
            nome = struct.unpack('100s', temp)[0]
            nome = nome.decode('utf-8').rstrip('\x00')
            print(nome)
            #idade
            temp = ficheiro.read(4)
            idade = struct.unpack('i',temp)[0]
            print (idade)
            #email
            temp = ficheiro.read(64)
            email = struct.unpack('64s', temp)[0]
            email = email.decode('utf-8').rstrip('\x00')
            print(email)
            #telefone
            temp = ficheiro.read(9)
            telefone = struct.unpack('9s', temp)[0]
            telefone = telefone.decode('utf-8').rstrip('\x00')
            print(telefone)
            print("="*25)

def menu_maker(titulo,opções,estilo):
    """função que mostra um menu"""
    print (estilo*25)
    print (titulo)
    print (estilo*25)

    for i in range(len(opções)):
        print (f"{i+1} - {opções[i]}")
    print (estilo*25)


def main():
    while True:
        menu_maker("menu",["adicionar","editar","remover","listar"],"=")
        op = int(input("opção: "))
        if op == 1:    
            adicionar()
        elif op == 2:
            editar()
        elif op == 3:
            remover()
        elif op == 4:
            listar()
        else:
            break

if __name__ =="__main__":
    main()
