def crear_repetits(a,b):
    c = b*int(a)
    return c

def crear_punts(a):
    for e in a:
        c=crear_repetits(int(e),'.')
        print(c)

a = input("Escriu una llista numèrica d'elements: ")
crear_punts(a)

