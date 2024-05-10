jogo = "___ | ___ | ___"  
fim = True

jogador2 = True
while fim == True:
    jogador1 = True
    while jogador1 == True: 
        print ("JOGADOR 1- escolha a posição em que deseja jogar (de 1 a nove) na linha abaixo")
        jogada = int(input(""))
        if jogada == 1 and jogo[0] == "_":
            jogo = "X" +jogo[1] + jogo[2] + jogo[3] + jogo[4] + jogo[5] + jogo[6] + jogo[7] + jogo[8] + jogo[9] + jogo[10] + jogo[11] + jogo[12]  + jogo[13] + jogo[14]
            print (jogo)
            jogador1 = False
        if jogada == 2 and jogo[1] == "_":
            jogo = jogo[0] + "X" + jogo[2] + jogo[3] + jogo[4] + jogo[5] + jogo[6] + jogo[7] + jogo[8] + jogo[9] + jogo[10] + jogo[11] + jogo[12]  + jogo[13] + jogo[14]
            print (jogo)
            jogador1 = False
        if jogada == 3 and jogo[2] == "_":
            jogo = jogo[0] + jogo[1] + "X" + jogo[3] + jogo[4] + jogo[5] + jogo[6] + jogo[7] + jogo[8] + jogo[9] + jogo[10] + jogo[11] + jogo[12]  + jogo[13] + jogo[14]
            print (jogo)
            jogador1 = False
        if jogada == 4 and jogo[6] == "_":
            jogo = jogo[0] + jogo[1] + jogo[2] + jogo[3] + jogo[3] + jogo[4] + jogo[5] + "X" + jogo[7] + jogo[8] + jogo[9] + jogo[10] + jogo[11] + jogo[12]  + jogo[13] + jogo[14]
            print (jogo)
            jogador1 = False
        if jogada == 5 and jogo[7] == "_":
            jogo = jogo[0] + jogo[1] + jogo[2] + jogo[3] + jogo[4] + jogo[5] + jogo[6] + "X" + jogo[8]+ jogo[9] + jogo[10] + jogo[11] + jogo[12]  + jogo[13] + jogo[14]
            print (jogo)
            jogador1 = False
        if jogada == 6 and jogo[8] == "_":
            jogo = jogo[0] + jogo[1] + jogo[2] + jogo[3] + jogo[4] + jogo[5] + jogo[6] + jogo[7] + "X" + jogo[9] + jogo[10] + jogo[11] + jogo[12]  + jogo[13] + jogo[14]
            print (jogo)
            jogador1 = False
        if jogada == 7 and jogo[12] == "_":
            jogo = jogo[0] + jogo[1] + jogo[2] + jogo[3] + jogo[4] + jogo[5] + jogo[6] + jogo[7] + jogo[8]+ jogo[9] + jogo[10] + jogo[11] + "X"  + jogo[13] + jogo[14]
            print (jogo)
            jogador1 = False
        if jogada == 8 and jogo[13] == "_":
            jogo = jogo[0] + jogo[1] + jogo[2] + jogo[3] + jogo[4] + jogo[5] + jogo[6] + jogo[7] + jogo[8]+ jogo[9] + jogo[10] + jogo[11] + jogo[12]  + "x" + jogo[14]
            print (jogo)
            jogador1 = False
        if jogada == 9 and jogo[14] == "_":
            jogo = jogo[0] + jogo[1] + jogo[2] + jogo[3] + jogo[4] + jogo[5] + jogo[6] + jogo[7] + jogo[8]+ jogo[9] + jogo[10] + jogo[11] + jogo[12]  + jogo[13] + "X"
            print (jogo)
            jogador1 = False
        print ("DADOS INVÁLIDOS!")
    jogador2 = True
    while jogador2 == True:
        print ("JOGADOR 2- escolha a posição em que deseja jogar (de 1 a nove) na linha abaixo")
        jogada = int(input(""))
        if jogada == 1 and jogo[0] == "_":
            jogo = "O" +jogo[1] + jogo[2] + jogo[3] + jogo[4] + jogo[5] + jogo[6] + jogo[7] + jogo[8] + jogo[9] + jogo[10] + jogo[11] + jogo[12]  + jogo[13] + jogo[14]
            print (jogo)
            jogador2 = False
        if jogada == 2 and jogo[1] == "_":
            jogo = jogo[0] + "O" + jogo[2] + jogo[3] + jogo[4] + jogo[5] + jogo[6] + jogo[7] + jogo[8] + jogo[9] + jogo[10] + jogo[11] + jogo[12]  + jogo[13] + jogo[14]
            print (jogo)
            jogador2 = False
        if jogada == 3 and jogo[2] == "_":
            jogo = jogo[0] + jogo[1] + "O" + jogo[3] + jogo[4] + jogo[5] + jogo[6] + jogo[7] + jogo[8] + jogo[9] + jogo[10] + jogo[11] + jogo[12]  + jogo[13] + jogo[14]
            print (jogo)
            jogador2 = False
        if jogada == 4 and jogo[6] == "_":
            jogo = jogo[0] + jogo[1] + jogo[2] + jogo[3] + jogo[4] + jogo[5] + "O" + jogo[7] + jogo[8] + jogo[9] + jogo[10] + jogo[11] + jogo[12]  + jogo[13] + jogo[14]
            print (jogo)
            jogador2 = False
        if jogada == 5 and jogo[7] == "_":
            jogo = jogo[0] + jogo[1] + jogo[2] + jogo[3] + jogo[4] + jogo[5] + jogo[6] + "O" + jogo[8]+ jogo[9] + jogo[10] + jogo[11] + jogo[12]  + jogo[13] + jogo[14]
            print (jogo)
            jogador2 = False
        if jogada == 6 and jogo[8] == "_":
            jogo = jogo[0] + jogo[1] + jogo[2] + jogo[3] + jogo[4] + jogo[5] + jogo[6] + jogo[7] + "O" + jogo[9] + jogo[10] + jogo[11] + jogo[12]  + jogo[13] + jogo[14]
            print (jogo)
            jogador2 = False
        if jogada == 7 and jogo[12] == "_":
            jogo = jogo[0] + jogo[1] + jogo[2] + jogo[3] + jogo[4] + jogo[5] + jogo[6] + jogo[7] + jogo[8]+ jogo[9] + jogo[10] + jogo[11] + "O"  + jogo[13] + jogo[14]
            print (jogo)
            jogador2 = False
        if jogada == 8 and jogo[13] == "_":
            jogo = jogo[0] + jogo[1] + jogo[2] + jogo[3] + jogo[4] + jogo[5] + jogo[6] + jogo[7] + jogo[8]+ jogo[9] + jogo[10] + jogo[11] + jogo[12]  + "O" + jogo[14]
            print (jogo)
            jogador2 = False
        if jogada == 9 and jogo[14] == "_":
            jogo = jogo[0] + jogo[1] + jogo[2] + jogo[3] + jogo[4] + jogo[5] + jogo[6] + jogo[7] + jogo[8]+ jogo[9] + jogo[10] + jogo[11] + jogo[12]  + jogo[13] + "O"
            print (jogo)
            jogador2 = False
        print ("DADOS INVÁLIDOS!")
        print (jogo)
    if (jogo[0] == jogo[1] and jogo[0] == jogo[2]) or (jogo[6] == jogo [7] and jogo [6] == jogo[8]) or (jogo[12] == jogo[13] and jogo [12] == (jogo[14])) or ((jogo[0] == jogo[6]) and (jogo [0] == jogo[12]) or (jogo[0] == jogo[7] and jogo[0] == jogo[14]) ):
        break