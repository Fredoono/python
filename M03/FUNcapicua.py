def main():
    capicua("fred")

def capicua(palav):
    invert = ""
    for letra in (palav):
        invert = letra + invert
    invert = invert.lower()
    palav = palav.lower()
    if invert == palav:
        print ("é uma capicua") 
    else:
        print ("não é uma capicua")

if __name__ == "__main__":
    main()  