# temos um restaurante com 100 vagas e 20 mesas
v = 100
m = 20
while v != 0:
    l = int(input("quantas pessoas entram? "))
    v = v - l
    m = m-1
    print ("ainda faltam",m,"mesas")
    print ("ainda faltam",v,"lugares")
    if l == 0 or m == 0:
        break
    if v > 0:
        print ("não á lugares suficientes")
    print ("insira 1 para inserirpessoas no restaurante; insira 2 para retirar pessoas dorestaurante")
    c = int(input("insira aqui: "))
    #retirar pessoas
    if c == 2:
        while v != 100:
            l = int(input("quantas pessoas se retiram? "))
            if v > 0:
                print ("não á tantas pessoas para tetirar")
            else:
                v = v + l
                m = m+1
                print ("ainda temos",m,"mesas")
                print ("ainda temos",v,"lugares")
                print ("insira 1 para inserirpessoas no restaurante; insira 2 para retirar pessoas dorestaurante")
                c = int(input("insira aqui: "))
                if v > 0:
                    print ("não á tantas pessoas para tetirar")
                if c == 1:
                    break