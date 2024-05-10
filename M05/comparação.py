#Programa para sugerir a loja onde um cabaz de produtos é mais barato
#O utilizador insere um cabaz de produtos a comprar
#Se não existirem todos os produtos a comprar deve informar o utilizador
precos = {"Pingo Doce":{"Arroz": 1.18, "Maçã": 2.85, "Leite": 0.82, "Frango": 4.98, "Café": 22.9, "Água5l": 1.29, "Azeite": 9.90, "Sal grosso": 0.25, "Açucar": 7.30, "Salmão": 12.99},
          "Auchan" : {"Frango":2.34,"Arroz":1.05,"Maçã":1.59,"Leite":0.80,"Azeite":12.68,"Água5l":1.05,"Água6l":0.84,"Sal grosso":2.29,"Salmão":24.93,"Açucar":1.79,"Café":6.59},
          "continente" :{"Arroz":1.83,"Maçã":1.99,"Leite":0.82,"Frango":1.25,"Café":6.59,"Água5l":1.05,"Água6l":0.84}
          }

def ProduteExiste(produto):
    for loja,produtos in precos.items():
        if produto in produtos:
            return True
    return False
def adicionar_ao_cabaz():
    cabaz = {}
    while True:
        compra = input("insira o produto que quer adicionar ao cabaz: ")
        if compra == "":
            break
        if not ProduteExiste(compra):
            print("não existe este produto em nenhuma loja")
        quantidade = float(input("insira quantos quer comprar: "))
        if quantidade <= 0:
            print ("a quantidade tem que ser maior que zero.")
            pass
        cabaz [compra] = quantidade
    return cabaz
cabaz = adicionar_ao_cabaz()
print (cabaz)
def comparar_precos(cabaz):
    comparação = {}
    for compra,quantidade in cabaz.items():
        for chave,valor in precos.items():
            soma = 0
            if compra in valor.keys():
                soma += valor[compra] * quantidade
            else:
                comparação[precos] = 100000000000000000000000000000000

            if chave in comparação:
                comparação[chave] += soma
            else:
                comparação[chave] = valor[compra] * quantidade
    return comparação
total_precos = (comparar_precos(cabaz))
def menor():
    maior = 0
    loja = ""
    for chave,valor in total_precos.items():
        if valor > maior:
            maior = valor
            loja = chave
    return (loja)
print(total_precos)