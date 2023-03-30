def llegir():
    llista=[]
    a = 'a'
    while(a!='.'):
        a = input ("Introducir un número: ")
        if a !='.':
            llista.append(int(a))
    return tuple(llista)

def mostrar_mayores_que(a,num):
    for e in a:
        if e>num:
            print(e)
        
#pp
x=llegir()
i = input("Introducir el número que desea comparar: ")
mostrar_mayores_que(x,int(i))