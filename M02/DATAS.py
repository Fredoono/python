import datetime
hoje = datetime.date.today()
print (hoje.month)
print (hoje.year)
print (hoje.day)

print (datetime.datetime.now().strftime("%H:%m:%S"))
#calcular a diferença entre duas datas
data1 = "2000-01-01"
data2 = "2008-01-04"

#converter para objetos datetime
data1_obj = datetime.datetime.strptime(data1,"%Y-%m-%d")
data2_obj = datetime.datetime.strptime(data2,"%Y-%m-%d")

diferença = data2_obj - data1_obj

print(diferença.days)