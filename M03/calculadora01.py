def soma(x,y):
    a = x + y
    return a
def subt(x,y):
    a= x-y
    return a
def multip (x,y):
    a= x*y
    return a
def divisão(x,y):
    a= x/y
    return a
def menu():
    op = (input("1-somar /n 2.subtraír /n 3.multiplicar /n 4dividir: "))
    n1 = float(input("um valor"))
    n2 = float(input("outro valor"))        
    if op == "1":
        print (soma(n1,n2))
    elif op == "2":
        print (subt(n1,n2))
    elif op == "3":
        print (multip(n1,n2))
    elif op == "4":
        print (divisão(n1,n2))
def main():
    menu()
if __name__== "__main__":
    main()
