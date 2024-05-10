dia = int(input("INSERE O DIA: "))
if dia >= 256 and dia <= 355:
    print ("outono")
if (dia <= 78 and dia > 0) or (dia < 355 and dia >= 366):
    print ("inverno")
if dia >= 172 and dia <= 264:
    print ("verão")
else:
    print ("primavera")