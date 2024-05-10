sen = input("insira a sua palavra passe: ")
regras = 0
regras1 = 1
regras2 = 2
regras3 = 3
regras4 = 4
if len(sen) <7:  
    print ("a senha é fraca")
else:
    for C in sen:
        if "1234567890" in C:   
            regras1 = 1
        elif "QWERTYUIOPÇLKJHGFDSAZXCVBNM" in C:
            regras2 = 1
        elif "qwertyuiopçlkjhgfdsaxcvbnm" in C:
            regras3 = 1
        elif "#&$@%!?;:.-_=+*<>\\/^~[](){;}" in C:
            regras4 = 1
        regras = regras1 + regras2+regras3+regras4
        if regras == 1:
            print ("a senha é fraca falta-lhe ódio")
        elif regras <= 3:
            print ("a senha é média")
        else:
            print ("a senha é forte")
