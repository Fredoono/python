import datetime

a = int(input("insira o ano em que nasceu: "))
d = int(input("insira o dia em que nasceu: "))
m = int(input("insira o mes em que nasceu: "))
hoje = datetime.date.today()
M = hoje.year
D = hoje.month
A = hoje.day 
idade = a - A
if m > M or (m == M and d > D):
    idade = idade -1
print (f"tem {idade} anos.")