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
    pass

def editar():
    if os.path.exists("agenda.bin")== False:
        return
    posição = int(input("insira o nome de quem quer apagar"))
    with(open("agenda.bin","rb+")) as ficheiro:
        ficheiro.seek(posição)
        dados_binarios = ficheiro.read(177)
        if not dados_binarios:
            return
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
