import datetime
q = input ("insira o dinheiro que ganha por dia: ")
d1 = input ("insira as datas em que começou e trabalhar: ")
d2 = input ("insira a data em que acabou de trabalhar: ")
d1_obj = datetime.datetime.strptime(d1,"%Y-%m-%d")
d2_obj = datetime.datetime.strptime(d2,"%Y-%m-%d")

dif = d2_obj - d1_obj 
if  dif == d2_obj - d1_obj  < 0:
    print ("datas não são validas")
else:
    print (f"trabalhou {dif.days}dias e vai ganhar {q * dif.days}")