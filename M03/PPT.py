import random

def Bot():
    num = random.randint(1,3)
    if num == 1:
        jogada = 1
    elif num == 2:
        jogada = 2
    else:
        jogada = 3
    return (jogada)

def Player():
    num = int(input("escolha 1 para pedra, 2 para papel, 3 para tesoura"))
    if num == 1:
        return (1)
    if num == 2:
        return (2)
    if num == 3:
        return (3)

def vitoria(bot,pess):
    if pess == 1:
        if bot == 1:
            return "empate"
        elif bot == 2:
            return "derrota"
        else:
            return "vitoria"
    if pess == 2:
        if bot == 1:
            return "derrota"
        elif bot == 2:
            return "empate"
        else:
            if bot == 3:
                return "vitoria"
    if pess == 3:
        if bot == 1:
            return "vitoria"
        elif bot == 2:
            return "empate"
        else:
            if bot == 3:
                return "derrota"

def main():
    while True:
        
        print(Player (escolha))
        print (vitoria (Bot(),Player(escolha)))
        print ("---------------------------------------")



if __name__ == "__main__":
    main()