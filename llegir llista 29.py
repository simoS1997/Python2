def llegir():
    l = []
    a = 'a'
    while a !='.':
        a = input("Pon el nombre: ")
        if a !='.':
            l.append (int(a))
    
    return l

def ncp(l,c):
    p = []
    x = 0
    for e in l:
        if e[0] == c:
            x += 1
            p.append(e)
    print( "El numero de paraules que comença {} són {} i són {}", format(c,x,p) )

#pp
a = llegir ()
c = input("Introduce el ")
ncp(a,c)