import math 

def distancia(x1,y1,x2,y2):
    comp = x2 -x1
    alt = y2-y1
    comp = comp * comp 
    alt = alt * alt
    dist = alt + comp
    dist = math.sqrt(dist)
    print (dist)

def main():
    distancia(1,2,4,6)

if __name__ == "__main__":
    main()
