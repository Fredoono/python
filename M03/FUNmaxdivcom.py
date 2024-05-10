def MDC(num1,num2):
    if num1 > num2:
        menor = num2
    else:
        menor = num1
    for i in range (menor,0, -1):
        if num1 % i == 0 and num2 % i == 0:
            mdc = i
            break
    print (mdc)

def main():
    MDC(20,50)

if __name__ == "__main__":
    main()
    