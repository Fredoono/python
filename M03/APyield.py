def gerarpares(limite):
    i = 0
    while i <= limite:
        yield i
        i += 2 

for numeroPar in gerarpares(111):
    print (numeroPar)