nome = "Oono-chan"
r = 0
x = 5
y = 10
def cumprimento3():
    print (f"bom dia {nome}")
def soma():
    global r,x,y
    r=x+y
    x = 0
def main():
    #cumprimento3()
    global x,y
    x = 4
    y = 4
    soma()
    print (r)
if __name__ == "__main__":
    main()