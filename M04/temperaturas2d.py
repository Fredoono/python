"""
um programa que le do utilisador as tempeeraturas mais elvedas de 3 cidades
o programa deve mostrar a temperatura mais elevada
"""
import numpy as np
MAX_ITEMS=(3,12)
temperaturas = np.zeros(MAX_ITEMS)
def entrada(arr):
#arr.shpae[0] indica quantas linhas tem o array
    for linhas in range (arr.shape[0]):
        for colunas in range(arr.shape[1]):
            temp = float(input(f"intruduza a temperatura da cidade {linhas+1} do mês {colunas+1}: "))
            arr[linhas,colunas] = temp
    return arr
def output(arr):
#procurar a temperatura mais elevada
    maior_temp= arr[0,0]
    for linhas in range (arr.shape[0]):
        for colunas in range (arr.shape[1]):
            if arr[linhas,colunas] > maior_temp:
                maior_temp == arr[linhas,colunas]
    print (f"a maior temperatura é {maior_temp}")
#calcular a média das temperaturas
    média = 0
    for linhas in range (arr.shape[0]):
        for colunas in range (arr.shape[1]):
            média += arr[linhas,colunas]
    média = média / (arr.shape[0]* arr.shape[1])
    print (f"a média total das temperaturas é {média}")
#calculas a média das temperaturas por cidade e mostrar a maior média
    for linhas in range (arr.shape[0]):
        soma = 0
        for colunas in range (arr.shape[0]):
            soma += arr[linhas,colunas]
            print (f"a média da cidade {colunas+1} é {soma/arr.shape[1]}")
            if linhas == 0 or maior_temp > média:
                maior_temp = soma/arr.shape[1]
                cidade = linhas
                print (f"a cidade com maiores temperaturas foi {cidade}")

#calcularr a média da temperatura por meses
    for colunas in range (arr.shape[1]):
        soma = 0
        for linnhsa in range(arr.shape[0]):
            soma += arr[linhas,colunas]
        media = soma/3
        if colunas == 0 or media> maior_media:
            maior_media = media
            mes = colunas
            print(f"a media da temperatura do mes {colunas} foi {media:.1f} ")

arrai = entrada(temperaturas)
output(arrai)
