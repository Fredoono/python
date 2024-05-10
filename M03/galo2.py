def player():
    while True:
        play = input("escolha a X ou Y para ser o seu jogador: ")
        if play == "x" or play == "X":
            return "x"
        elif play == "y" or play == "Y":
            return "y"
        else:
            print ("dados inválidos")

jogo = f"{1}"


def main():
    player()


if __name__ == "__main__":
    main()