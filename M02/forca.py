p = "aljubarrota"
t = 8
pj = "_"*len(p)

print ("vamos jogar ao jogo da froca :)")
while t > 0:
    L = input("insira a letra desejada: ").lower()
    temp = ""
    acertou = False
    for i in range(len(p)): 
        if L == p[i]:
            temp += L
            acertou = True
        else:
            temp += pj[i]
    if acertou == False:
        t -= 1
    if pj == p:
        print (f"acertou a palavra era {p}")
        break
    pj = temp 
    print (pj)
    print (f"tentativas restantes {t}")
if t == 0:
    print (f"perdeste a palavra correta é {p}")
