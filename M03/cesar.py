def codificar(palav):
    abc = "abcdefghijklmnopqrstuvwxyz"
    bcd = "bcdefghijklmnopqrstuvwxyza"
    codigo = ""
    for letra in (palav):
        if letra in abc:
            posicao = abc.index(letra)  
            codigo = codigo + bcd[posicao]
        else:
            codigo = codigo + letra
    print (codigo)

def descodificar(palav):
    abc = "abcdefghijklmnopqrstuvwxyz"
    bcd = "bcdefghijklmnopqrstuvwxyza"
    descodigo = ""
    for letra in (palav):
        if letra in bcd:
            posicao = bcd.index(letra)  
            descodigo = descodigo + abc[posicao]
        else:
            descodigo = descodigo + letra
    print (descodigo)
codificar("fred")
descodificar("gsfe")