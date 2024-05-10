import sys
def Qvogais(palav):
    palav = palav.lower()
    vogais = 0
    for letra in (palav):
        if "aeiouáéíóúãõâêîôûàèìùò" in palav:
            vogais = vogais +1
    print (vogais)

if len(sys.argv) == 2:

    Qvogais(sys.argv[1])
else:
    UserInput = input("escreva uma palavra: ")
    Qvogais(UserInput)
    
