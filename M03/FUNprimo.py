

def num_pri(num):
    tres = 0
    for i in range (1,num+1):
        if num % i == 0:
            tres = tres + 1
    if tres == 2:
        print ("é primo")
    else:
        print ("nao é primo")
num_pri(2)