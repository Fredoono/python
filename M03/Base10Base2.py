def conB10(num):
    soma = 0
    expoe = len(num)
    for posicao in num:
        if num[posicao] == "1":
            soma = soma + 2 ** expoe
        expoe -= 1
    return soma
print (conB10("1011"))

