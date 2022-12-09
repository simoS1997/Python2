# Definim una funció
def Reves(a):
    # Indicam quina ha de ser la variable
    b = ''

    # Ordenam quin és el loop
    for x in a:
        # Aqui giram l'ordre
        b = x + b
    return b

opcio = input ("Escriu que vols al reves: ")

# Aqui sortiràn els resultats
print('Text original: ', opcio)
print('Text canviat: ', Reves(opcio))