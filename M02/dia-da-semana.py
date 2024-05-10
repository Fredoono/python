import datetime
ano = int(input ("insira o ano em que nasceu: "))
dia = int(input ("insira o dia em que nasceu: "))
mes = int(("insira o mes em que nasceu: "))
data = datetime.date(ano,mes,dia)

print (data.weekday())

print (data.strftime("%A"))
