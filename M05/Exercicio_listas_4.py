#Exercicio_listas_4.py
n = (input("data de nascimento: "))
n = n.split("/")
n = int(n[2])
n = ((n-1900)%12)
print (n)
lista = ["o signo é rato", "o signo é búfalo", "o signo é tigre", "o signo é coelho", "o signo é dragão", "o signo é serpente", "o signo é cavalo", "o signo é cabra", "o signo é macaco", "o signo é galo", "o signo é cachorro", "o signo é porco"]
print (lista[n])