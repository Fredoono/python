soma_temperaturas = 0
i = 1
maior_temperatura = -float("inf")
menor_temperatura = float("inf")
contar_negativas = 0
while i < 6:
    temperatura = float(input(f'Insira a temperatura (de -50 a 50) {i}: '))
    soma_temperaturas += temperatura
    if temperatura < -50 or temperatura > 50:
        print ("dados inválidos (de -50 a 50)")
        continue
    if temperatura > maior_temperatura:
        maior_temperatura = temperatura
    if temperatura < menor_temperatura:
        menor_temperatura = temperatura
    i += 1
    if temperatura < 0:
        contar_negativas = contar_negativas +1
media_temperaturas = soma_temperaturas / 5

print(f'A menor temperatura é: {menor_temperatura}')
print(f'A média das temperaturas é: {media_temperaturas}')
print(f'A maior temperatura é: {maior_temperatura}')    
print (f"há {contar_negativas} temperaturas negativas e {5 - contar_negativas} temperaturas positivas")
