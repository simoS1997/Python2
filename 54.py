def elements_parells(llista):
    parells = []
    for index, element in enumerate(llista):
        if index % 2 == 0:
            parells.append(element)
    return parells

llista = input("Introdueix una llista de paraules separades per espais: ").split()
parells = elements_parells(llista)
print(parells)
