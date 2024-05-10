#calcular os dias até ao fim do mês
r = 0
while True:
    h = int(input("insira o dia de hoje: "))
    if h < 1 or h > 31:
        print ("dados inválidos")
        continue
    m = int(input("qual é o mês: "))
    if m < 1 or m > 12:
        print ("dados inválidos")
        continue
    if m == (1,3,5,7,8,10,12):
        r = 31 - h
    elif m == 2:
        r = 28 - h
    else:
        r = 30 - h
    if r < 0 or h < 1:
        print (" o dia é inválido")
    else: 
        break
print (r)

