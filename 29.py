def llegir_noms():
    i=0
    l=[]
    print("Introdueixi noms a la llista, per acabar posau -1: ")
    while i>-1:
        l.append(input("Posi el següent nom: "))
        if (l[i]=="-1"):
            l.remove("-1")
            i=-5
        i+=1
    return l


def llegir_noms():
    i=0
    l=[]
    print("Introdueixi noms a la llista, per acabar posau -1: ")
    while True:
        nom = input("Posi el següent nom: ")
        if nom == "-1":
            break
        l.append(nom)
    return l
    
# Programa principal
noms = llegir_noms()
caracter = input("Introdueixi el caràcter que vols que comencin les paraules a cercar: ")
llegir_noms(noms,caracter)

