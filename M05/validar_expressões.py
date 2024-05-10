import sys
argv = sys.argv
if len (argv)==1:
    conta = ""
else:
    conta = argv[1]

def validar_conta(conta):
    dic = {
        "(":")",
        "[":"]",
        "{":"}"
    }
    validar = []
    for i in range(len(conta)):
        if conta[i] in "([{":
            validar += conta[i]
        if conta[i] in "}])":
            validar += conta[i]
            print (validar)
            if validar[0] == "":
                print ("não validado")
                break
            if dic[validar[0]]!= validar[1]:
                print ("nao validado")
    if len(validar) != 0:
        print ("nao validado")
validar_conta(conta)