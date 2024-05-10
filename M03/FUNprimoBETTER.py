def primo(num):
    for i in range(2,num):
        resto = num%i
        if resto == 0:
            print ("não é primo")
            return
    print ("é primo")