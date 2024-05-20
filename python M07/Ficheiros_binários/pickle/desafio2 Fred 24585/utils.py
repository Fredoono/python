"""mudo para funções gerais e práticas"""
#trabalho realizado por Frederico Sousa 10ºT nº8 2024

def lersonumeros(msg):
    """função que le e devolve apenas numeros inteiros"""
    numer = input(msg)
    while not numer.isnumeric():
        print("opção inválida")
        numer = input(msg)
    return int(numer)


def lersotexto(msg,minimo=1):
    """função que le e devolve texto"""
    text = input(msg)
    while text is not None and len(text) < minimo:
        print("opção inválida")
        text = input(msg)
    return text


def menu_maker(titulo,opções,estilo):
    """função que mostra um menu"""
    print (estilo*25)
    print (titulo)
    print (estilo*25)

    for i in range(len(opções)):
        print (f"{i+1} - {opções[i]}")
    print (estilo*25)
    